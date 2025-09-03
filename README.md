# Palópoli & Albrecht - Site Institucional

Projeto contendo o frontend em React/Vite e o backend em Python/Flask para o site da Palópoli & Albrecht.

## 🚀 Funcionalidades

- **Blog** com artigos sobre direito
- **Equipe** com perfis dos advogados
- **Áreas de Atuação** detalhadas
- **Publicações** e artigos
- **Contato**

## 🏗️ Estrutura do Projeto

- `frontend/` – Aplicação React com TailwindCSS
- `backend/` – API Python com Flask e SQLite
  - `public/` – Build estático do frontend servido pelo Express
  - `routes/` – Rotas da API
  - `sql/` – Esquemas do banco de dados
  - `db_operations.py` – Operações do banco de dados
- `.github/workflows/` – CI/CD

## 🛠️ Configuração do Ambiente

### Pré-requisitos

- Node.js 18+
- Python 3.8+
- SQLite3

### Configuração do Backend

1. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. Instale as dependências:
   ```bash
   pip install -r backend/requirements.txt
   ```

3. Inicie o servidor de desenvolvimento:
   ```bash
   cd backend
   python app.py
   ```

### Configuração do Frontend

1. Instale as dependências:
   ```bash
   cd frontend
   npm install
   ```

2. Inicie o servidor de desenvolvimento:
   ```bash
   npm run dev
   ```

## 🚀 Deploy

O projeto está configurado para deploy automático via GitHub Actions. O workflow `deploy.yml` executa as seguintes etapas:

1. Build do frontend
2. Upload dos arquivos estáticos via FTP
3. Upload do backend

### Variáveis de Ambiente Necessárias

Configure os seguintes segredos no repositório:

- `FTP_HOST` - Endereço do servidor FTP
- `FTP_USER` - Usuário FTP
- `FTP_PASSWORD` - Senha FTP
- `FTP_REMOTE_DIR` - Diretório remoto no servidor

## 📦 Banco de Dados

O backend utiliza MySQL. Crie um arquivo `.env` na raiz do projeto ou no diretório `backend/` com as seguintes variáveis:

```
DB_HOST=localhost
DB_PORT=3306
DB_NAME=palopoli
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```

Em produção, adicione essas variáveis ao ambiente do serviço Node.js (por exemplo, no painel do Plesk) para evitar falhas de conexão.

### Inicialização do Banco de Dados

Com o `.env` configurado, instale o esquema e dados iniciais:

```bash
npm --prefix backend run db:setup
```

## 🤝 Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request
