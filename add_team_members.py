import sys
import os
# Adiciona o diretório backend ao PATH para encontrar o módulo db_operations
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
from db_operations import DatabaseManager
from datetime import datetime

def add_team_members():
    # Configuração do banco de dados SQLite
    db_config = {
        'database': 'palopoli.db'
    }
    
    # Inicializa o gerenciador de banco de dados
    db = DatabaseManager(db_config)
    
    if not db.connect():
        print("Não foi possível conectar ao banco de dados.")
        return
    
    # Lista de membros da equipe
    team_members = [
        {
            'name': 'Jéssica dos Santos Araújo',
            'email': 'jessica.araujo@palopoli.adv.br',
            'role': 'Advogada',
            'bio': 'Especialista em Direito Civil, Multipropriedade, Direito do Consumidor e Direito de Família. Experiência em litígios cíveis, bancários, família e consumeristas.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2025-02-01'
        },
        {
            'name': 'Valéria Costa Barbosa De Souza',
            'email': 'valeria.souza@palopoli.adv.br',
            'role': 'Advogada',
            'bio': 'Especialista em Direito Cível, Multipropriedade e Direito do Consumidor. Experiência em litígios cíveis, bancários e consumeristas.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2025-04-01'
        },
        {
            'name': 'Damaris da Silva de Sousa',
            'email': 'damaris.sousa@palopoli.adv.br',
            'role': 'Advogada',
            'bio': 'Atuação em Consultivo e Contencioso Cível, com foco em Direito do Consumidor, Família e Sucessões.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2025-03-01'
        },
        {
            'name': 'Nicóle Ariel de Oliveira',
            'email': 'nicole.oliveira@palopoli.adv.br',
            'role': 'Advogada',
            'bio': 'Especialista em Contencioso e Estratégico Cível, com experiência em cumprimento de sentença, rescisões contratuais e interposição de recursos em instâncias superiores.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2023-08-01'
        },
        {
            'name': 'Jaqueline Araujo Rodrigues',
            'email': 'jaqueline.rodrigues@palopoli.adv.br',
            'role': 'Advogada',
            'bio': 'Especialista em Direito do Trabalho, com experiência em consultivo, contencioso trabalhista e direito coletivo.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2024-04-01'
        },
        {
            'name': 'Mariana Zaroni Martins',
            'email': 'mariana.martins@palopoli.adv.br',
            'role': 'Analista Jurídica',
            'bio': 'Atua na Controladoria Jurídica, com foco em padronização, monitoramento de cadastros e prazos processuais.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2025-04-01'
        },
        {
            'name': 'Gabrielle Assayag Ribeiro',
            'email': 'gabrielle.ribeiro@palopoli.adv.br',
            'role': 'Advogada',
            'bio': 'Especialista em Contencioso Cível Estratégico, atuando em causas de média e alta complexidade nas áreas cível, empresarial e societário.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2024-03-01'
        },
        {
            'name': 'Ana Carolina Vieira Mota Souto',
            'email': 'carolina.souto@palopoli.adv.br',
            'role': 'Advogada',
            'bio': 'Especialista em Direito Civil Estratégico e Direito Empresarial, com atuação em contencioso civil estratégico, direito digital e arbitragem.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2024-09-01'
        },
        {
            'name': 'Mariana Aparecida Corrêa',
            'email': 'mariana.correa@palopoli.adv.br',
            'role': 'Advogada Trabalhista',
            'bio': 'Especialista em Direito do Trabalho, atuando em contencioso e consultivo trabalhista, com experiência em litígios de alta complexidade.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2022-09-01'
        },
        {
            'name': 'Paulo Fernando Chaves Jucá Rolim',
            'email': 'paulo.juca@palopoli.adv.br',
            'role': 'Advogado Sênior',
            'bio': 'Especialista em Direito Corporativo e Societário, com mais de 35 anos de experiência em gestão de equipes e operações societárias complexas.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2024-03-01'
        },
        {
            'name': 'Andressa Martins de Souza Ghesso',
            'email': 'andressa.souza@palopoli.adv.br',
            'role': 'Advogada',
            'bio': 'Especialista em Direito Cível e Contratos, com ampla experiência em litígios empresariais e elaboração de contratos.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2014-08-01'
        },
        {
            'name': 'Gabriela Miranda de Sousa',
            'email': 'gabriela.miranda@palopoli.adv.br',
            'role': 'Advogada',
            'bio': 'Especialista em Direito Cível, com experiência em contencioso cível e trabalhista, além de defesas administrativas.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2023-07-01'
        },
        {
            'name': 'Marlizy Elysa da Silva Cagnoni',
            'email': 'marlizy.cagnoni@palopoli.adv.br',
            'role': 'Advogada Trabalhista',
            'bio': 'Atua no contencioso e consultivo trabalhista, com experiência em elaboração de peças processuais e análise de riscos.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2023-01-01'
        },
        {
            'name': 'Marcos Gomes de Souza',
            'email': 'marcos.souza@palopoli.adv.br',
            'role': 'Advogado',
            'bio': 'Especialista em Controladoria Jurídica e Legal Operations, com experiência em gestão de processos e análise de dados.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2023-10-01'
        },
        {
            'name': 'Bárbara Teixeira Lima',
            'email': 'barbara.lima@palopoli.adv.br',
            'role': 'Advogada',
            'bio': 'Especialista em Direito Societário e Tributário, com experiência em criação e análise de contratos e atos societários.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2022-05-01'
        },
        {
            'name': 'Isabella Ferreira dos Santos',
            'email': 'isabella.santos@palopoli.adv.br',
            'role': 'Advogada',
            'bio': 'Atua no contencioso cível, com foco em direito do consumidor, multipropriedade, família e sucessões.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2024-03-01'
        },
        {
            'name': 'Ester Lemes de Siqueira Regis',
            'email': 'ester.lemes@palopoli.adv.br',
            'role': 'Advogada Sênior',
            'bio': 'Especialista em Direito do Trabalho, com ampla experiência em contencioso trabalhista, dissídios coletivos e negociações sindicais.',
            'phone': None,
            'avatar_url': None,
            'social_links': None,
            'join_date': '2012-01-01'
        }
    ]
    
    try:
        # Adiciona cada membro da equipe
        for member in team_members:
            # Verifica se o membro já existe pelo e-mail
            existing_members = db.get_team_members()
            email_exists = any(m['email'] == member['email'] for m in existing_members if 'email' in m)
            
            if not email_exists:
                # Adiciona o membro
                member_id = db.create_team_member(
                    name=member['name'],
                    role=member['role'],
                    bio=member['bio'],
                    email=member['email'],
                    phone=member['phone'],
                    avatar_url=member['avatar_url'],
                    social_links=member['social_links']
                )
                if member_id:
                    print(f"Adicionado: {member['name']} ({member['email']})")
                else:
                    print(f"Falha ao adicionar: {member['name']}")
            else:
                print(f"Membro já existe: {member['name']} ({member['email']})")
        
        print("\nProcesso de adição de membros concluído!")
        
    except Exception as e:
        print(f"Erro ao adicionar membros: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    add_team_members()
