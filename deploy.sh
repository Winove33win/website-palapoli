#!/bin/bash
set -e

# Script de deploy para o servidor de produção sem uso de sudo ou PM2

echo "Encerrando processos na porta 3333..."
if command -v lsof >/dev/null 2>&1; then
  lsof -t -i:3333 | xargs -r kill -9 2>/dev/null || true
else
  echo "lsof não encontrado, pulando encerramento de processos."
fi

# Navega até o diretório do projeto (raiz deste script)
PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"

# Atualiza o código do repositório se for um repositório Git
if [ -d "$PROJECT_ROOT/.git" ] && git -C "$PROJECT_ROOT" remote get-url origin >/dev/null 2>&1; then
  echo "Atualizando código do repositório..."
  git -C "$PROJECT_ROOT" pull origin main
fi

# Build do frontend
echo "Construindo frontend..."
cd "$PROJECT_ROOT/frontend"
npm install
npm run build
rm -rf "$PROJECT_ROOT/backend/public"
mkdir -p "$PROJECT_ROOT/backend/public"
cp -r dist/* "$PROJECT_ROOT/backend/public/"

# Instala as dependências do backend
echo "Instalando dependências do backend..."
cd "$PROJECT_ROOT/backend"
npm install

# Inicia o serviço
echo "Iniciando o serviço..."
NODE_ENV=production npm run start &

echo "Deploy concluído com sucesso!"
