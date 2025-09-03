#!/usr/bin/env python3
"""
Script para inicializar o banco de dados e adicionar dados de exemplo.

Este script cria as tabelas necessárias e popula o banco de dados com dados iniciais
para desenvolvimento e testes.
"""
import os
import sys
from datetime import datetime, timedelta

# Adiciona o diretório raiz ao path para importar os módulos
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.db_operations import DatabaseManager
from backend.database import create_tables

def add_sample_data():
    """Adiciona dados de exemplo ao banco de dados."""
    # Configuração do banco de dados
    db_config = {
        'database': os.path.join(os.path.dirname(__file__), 'palopoli.db')
    }
    
    # Cria uma instância do gerenciador de banco de dados
    db = DatabaseManager(db_config)
    
    try:
        # Conecta ao banco de dados
        if not db.connect():
            print("Erro ao conectar ao banco de dados.")
            return False
        
        print("Adicionando membros da equipe...")
        
        # Lista de membros da equipe
        team_members = [
            {
                'name': 'Dr. Carlos Palópoli',
                'role': 'Sócio Fundador',
                'bio': 'Advogado com mais de 20 anos de experiência em direito empresarial e tributário.',
                'email': 'carlos.palopoli@palopoli.adv.br',
                'phone': '+55 11 99999-9999',
                'avatar_url': '/images/team/palopoli.jpg',
                'social_links': {
                    'linkedin': 'https://linkedin.com/in/carlospalopoli',
                    'lattes': 'http://lattes.cnpq.br/1234567890123456'
                }
            },
            {
                'name': 'Dra. Ana Albrecht',
                'role': 'Sócia',
                'bio': 'Especialista em direito trabalhista e previdenciário com ampla atuação em grandes empresas.',
                'email': 'ana.albrecht@palopoli.adv.br',
                'phone': '+55 11 99999-8888',
                'avatar_url': '/images/team/albrecht.jpg',
                'social_links': {
                    'linkedin': 'https://linkedin.com/in/anaalbrecht',
                    'lattes': 'http://lattes.cnpq.br/6543210987654321'
                }
            },
            # Adicione mais membros conforme necessário
        ]
        
        # Adiciona os membros da equipe
        member_ids = {}
        for member in team_members:
            # Verifica se o membro já existe
            existing_member = db._fetch_one(
                "SELECT id FROM team_members WHERE email = ?",
                (member['email'],)
            )
            
            if existing_member:
                print(f"Membro {member['name']} já existe no banco de dados.")
                member_ids[member['name']] = existing_member['id']
            else:
                # Adiciona o novo membro
                member_id = db.create_team_member(
                    name=member['name'],
                    role=member['role'],
                    bio=member['bio'],
                    email=member['email'],
                    phone=member['phone'],
                    avatar_url=member['avatar_url'],
                    social_links=member.get('social_links')
                )
                
                if member_id:
                    print(f"Adicionado membro: {member['name']} (ID: {member_id})")
                    member_ids[member['name']] = member_id
                else:
                    print(f"Erro ao adicionar membro: {member['name']}")
        
        # Adiciona posts de exemplo se não existirem
        print("\nAdicionando posts de exemplo...")
        
        # Verifica se já existem posts
        existing_posts = db._fetch_all("SELECT slug FROM posts LIMIT 1")
        
        if existing_posts:
            print("Já existem posts no banco de dados. Pulando a adição de posts de exemplo.")
        else:
            # Lista de posts de exemplo
            sample_posts = [
                {
                    'title': 'As Novas Tendências do Direito Digital em 2025',
                    'slug': 'novas-tendencias-direito-digital-2025',
                    'category': 'Direito Digital',
                    'content': '<p>O Direito Digital está em constante evolução. Neste artigo, exploramos as principais tendências para 2025...</p>',
                    'excerpt': 'Confira as principais mudanças e tendências no Direito Digital para o próximo ano.',
                    'author_name': 'Dr. Carlos Palópoli',
                    'reading_time': 5,
                    'tags': ['Direito Digital', 'Tecnologia', 'LGPD'],
                    'featured': True
                },
                {
                    'title': 'Guia Completo sobre Multipropriedade',
                    'slug': 'guia-completo-multipropriedade',
                    'category': 'Direito Imobiliário',
                    'content': '<p>A multipropriedade é uma forma de propriedade que vem ganhando popularidade no Brasil...</p>',
                    'excerpt': 'Tudo o que você precisa saber sobre o regime de multipropriedade no Brasil.',
                    'author_name': 'Dra. Ana Albrecht',
                    'reading_time': 8,
                    'tags': ['Direito Imobiliário', 'Multipropriedade', 'Legislação'],
                    'featured': True
                },
                # Adicione mais posts conforme necessário
            ]
            
            # Adiciona os posts
            for post in sample_posts:
                # Obtém o ID do autor pelo nome
                author_id = None
                if post.get('author_name'):
                    author = db._fetch_one(
                        "SELECT id FROM team_members WHERE name = ?",
                        (post['author_name'],)
                    )
                    if author:
                        author_id = author['id']
                
                # Verifica se o post já existe
                existing_post = db._fetch_one(
                    "SELECT id FROM posts WHERE slug = ?",
                    (post['slug'],)
                )
                
                if existing_post:
                    print(f"Post '{post['title']}' já existe no banco de dados.")
                else:
                    # Adiciona o novo post
                    post_id = db.create_post(
                        slug=post['slug'],
                        title=post['title'],
                        category=post['category'],
                        content_html=post['content'],
                        author_id=author_id,
                        excerpt=post.get('excerpt'),
                        reading_time=post.get('reading_time'),
                        tags=post.get('tags'),
                        featured=post.get('featured', False),
                        status='published',
                        published_at=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    )
                    
                    if post_id:
                        print(f"Adicionado post: {post['title']} (ID: {post_id})")
                    else:
                        print(f"Erro ao adicionar post: {post['title']}")
        
        print("\nInicialização do banco de dados concluída com sucesso!")
        return True
        
    except Exception as e:
        print(f"Erro durante a inicialização do banco de dados: {e}")
        return False
    finally:
        # Fecha a conexão com o banco de dados
        db.close()

def main():
    """Função principal para inicialização do banco de dados."""
    print("=== INICIALIZAÇÃO DO BANCO DE DADOS ===\n")
    
    # Cria as tabelas se não existirem
    print("Criando tabelas...")
    if create_tables():
        print("Tabelas criadas com sucesso!")
    else:
        print("Erro ao criar as tabelas. Verifique o log para mais detalhes.")
        return False
    
    # Adiciona dados de exemplo
    print("\nAdicionando dados de exemplo...")
    return add_sample_data()

if __name__ == "__main__":
    if main():
        sys.exit(0)
    else:
        sys.exit(1)
