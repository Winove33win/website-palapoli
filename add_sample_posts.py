import sys
import os
from datetime import datetime, timedelta

# Adiciona o diretório backend ao PATH para encontrar o módulo db_operations
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from db_operations import DatabaseManager

def add_sample_posts():
    # Configuração do banco de dados SQLite
    db_config = {
        'database': 'palopoli.db'
    }
    
    # Inicializa o gerenciador de banco de dados
    db = DatabaseManager(db_config)
    
    if not db.connect():
        print("Não foi possível conectar ao banco de dados.")
        return
    
    try:
        # Obtém a lista de membros da equipe para usar como autores
        team_members = db.get_team_members()
        if not team_members:
            print("Nenhum membro da equipe encontrado. Adicione membros primeiro.")
            return
        
        # Lista de posts de exemplo
        sample_posts = [
            {
                'title': 'As Novas Tendências do Direito Digital em 2025',
                'slug': 'novas-tendencias-direito-digital-2025',
                'category': 'Direito Digital',
                'author_id': next((m['id'] for m in team_members if 'Nicóle' in m['name']), team_members[0]['id']),
                'content_html': '''
                    <p>O Direito Digital continua em constante evolução, e 2025 não é diferente. Neste artigo, exploramos as principais tendências que estão moldando o cenário jurídico digital:</p>
                    <h3>1. Regulamentação de IA</h3>
                    <p>Com o avanço da inteligência artificial, novas regulamentações estão sendo discutidas para garantir o uso ético e responsável dessas tecnologias.</p>
                    <h3>2. Privacidade de Dados</h3>
                    <p>A LGPD completa 5 anos e novas interpretações sobre o tratamento de dados pessoais continuam a surgir.</p>
                    <h3>3. Contratos Inteligentes</h3>
                    <p>Os smart contracts estão se tornando cada vez mais comuns, exigindo novas abordagens legais.</p>
                ''',
                'excerpt': 'Confira as principais tendências e desafios do Direito Digital em 2025, incluindo IA, privacidade de dados e contratos inteligentes.',
                'tags': ['Direito Digital', 'Tecnologia', 'LGPD', 'IA'],
                'reading_time': 5,
                'status': 'published',
                'featured': True,
                'published_at': (datetime.now() - timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                'title': 'Guia Completo sobre Multipropriedade',
                'slug': 'guia-completo-multipropriedade',
                'category': 'Direito Imobiliário',
                'author_id': next((m['id'] for m in team_members if 'Jéssica' in m['name']), team_members[0]['id']),
                'content_html': '''
                    <p>A multipropriedade é uma forma de propriedade que vem ganhando destaque no mercado imobiliário. Neste guia, explicamos:</p>
                    <h3>O que é Multipropriedade?</h3>
                    <p>Conceito e características principais deste modelo de negócio.</p>
                    <h3>Direitos e Deveres</h3>
                    <p>Quais são as obrigações e benefícios dos proprietários.</p>
                    <h3>Aspectos Legais</h3>
                    <p>Como a legislação brasileira trata a multipropriedade.</p>
                ''',
                'excerpt': 'Tudo o que você precisa saber sobre multipropriedade, desde conceitos básicos até aspectos legais importantes.',
                'tags': ['Multipropriedade', 'Direito Imobiliário', 'Legislação'],
                'reading_time': 7,
                'status': 'published',
                'featured': True,
                'published_at': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                'title': 'Mudanças na CLT em 2025: O que você precisa saber',
                'slug': 'mudancas-clt-2025',
                'category': 'Direito do Trabalho',
                'author_id': next((m['id'] for m in team_members if 'Ester' in m['name']), team_members[0]['id']),
                'content_html': '''
                    <p>O ano de 2025 trouxe importantes alterações na Consolidação das Leis do Trabalho. Neste artigo, abordamos:</p>
                    <h3>Novas Regras para Home Office</h3>
                    <p>Como ficou a regulamentação do trabalho remoto.</p>
                    <h3>Banco de Horas</h3>
                    <p>Mudanças na compensação de jornada de trabalho.</p>
                    <h3>Direitos dos Trabalhadores</h3>
                    <p>Novos direitos e benefícios para os empregados.</p>
                ''',
                'excerpt': 'Confira as principais alterações na CLT que entraram em vigor em 2025 e como elas afetam empregadores e empregados.',
                'tags': ['CLT', 'Direito do Trabalho', 'Legislação Trabalhista'],
                'reading_time': 6,
                'status': 'published',
                'featured': True,
                'published_at': (datetime.now() - timedelta(days=10)).strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                'title': 'Direito do Consumidor: Seus Direitos nas Compras Online',
                'slug': 'direito-consumidor-compras-online',
                'category': 'Direito do Consumidor',
                'author_id': next((m['id'] for m in team_members if 'Valéria' in m['name']), team_members[0]['id']),
                'content_html': '''
                    <p>As compras online continuam em alta, mas muitos consumidores desconhecem seus direitos. Neste artigo, explicamos:</p>
                    <h3>Arrependimento de Compra</h3>
                    <p>Como funciona o direito de arrependimento nas compras pela internet.</p>
                    <h3>Prazos de Entrega</h3>
                    <p>O que fazer quando o prazo de entrega não é cumprido.</p>
                    <h3>Produtos com Defeito</h3>
                    <p>Quais são os seus direitos ao receber um produto com defeito.</p>
                ''',
                'excerpt': 'Conheça seus direitos como consumidor nas compras online e saiba como agir em situações problemáticas.',
                'tags': ['Direito do Consumidor', 'Compras Online', 'CDC'],
                'reading_time': 4,
                'status': 'published',
                'featured': False,
                'published_at': (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d %H:%M:%S')
            },
            {
                'title': 'Aspectos Jurídicos da LGPD para Pequenas Empresas',
                'slug': 'lgpd-pequenas-empresas',
                'category': 'LGPD',
                'author_id': next((m['id'] for m in team_members if 'Paulo' in m['name']), team_members[0]['id']),
                'content_html': '''
                    <p>Muitas pequenas empresas ainda têm dúvidas sobre como se adequar à LGPD. Neste artigo, abordamos:</p>
                    <h3>Obrigações das Pequenas Empresas</h3>
                    <p>Quais são os principais requisitos da LGPD para PMEs.</p>
                    <h3>Como se Adequar</h3>
                    <p>Passos práticos para garantir a conformidade com a legislação.</p>
                    <h3>Multas e Penalidades</h3>
                    <p>Quais são as consequências do não cumprimento da LGPD.</p>
                ''',
                'excerpt': 'Guia prático para pequenas empresas entenderem e cumprirem as exigências da Lei Geral de Proteção de Dados.',
                'tags': ['LGPD', 'Proteção de Dados', 'Pequenas Empresas'],
                'reading_time': 8,
                'status': 'published',
                'featured': True,
                'published_at': (datetime.now() - timedelta(days=20)).strftime('%Y-%m-%d %H:%M:%S')
            }
        ]
        
        # Adiciona cada post
        for post_data in sample_posts:
            # Verifica se o post já existe pelo slug
            cursor = db.connection.cursor()
            cursor.execute("SELECT id FROM posts WHERE slug = ?", (post_data['slug'],))
            if not cursor.fetchone():
                # Adiciona o post
                post_id = db.create_post(
                    slug=post_data['slug'],
                    title=post_data['title'],
                    category=post_data['category'],
                    content_html=post_data['content_html'],
                    author_id=post_data['author_id'],
                    excerpt=post_data['excerpt'],
                    tags=post_data['tags'],
                    reading_time=post_data['reading_time'],
                    status=post_data['status'],
                    featured=post_data['featured'],
                    published_at=post_data['published_at']
                )
                if post_id:
                    print(f"Adicionado: {post_data['title']}")
                else:
                    print(f"Falha ao adicionar: {post_data['title']}")
            else:
                print(f"Post já existe: {post_data['title']}")
        
        print("\nProcesso de adição de posts concluído!")
        
    except Exception as e:
        print(f"Erro ao adicionar posts: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    add_sample_posts()
