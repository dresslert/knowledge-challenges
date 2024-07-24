# Plataforma de Desafios de Conhecimento com Gamificação

## Objetivo do Projeto

A **Plataforma de Desafios de Conhecimento com Gamificação** é uma aplicação web inovadora que permite aos usuários participar de desafios de conhecimento, receber feedback social e acompanhar seu progresso com elementos de gamificação.

## Funcionalidades Principais

- **Gestão de Desafios:** Crie e gerencie desafios de conhecimento em várias categorias.
- **Feedback Social:** Receba e forneça feedback sobre o progresso dos desafios.
- **Sistema de Pontuação:** Ganhe pontos e veja seu desempenho em tabelas de classificação.
- **Gamificação:** Desbloqueie conquistas e badges por completar desafios.
- **Personalização:** Adapte desafios com base em interesses e histórico.

## Tecnologias e Ferramentas Utilizadas

- **Backend:** FastAPI, SQLAlchemy
- **Frontend:** Jinja2, Tailwind CSS
- **Banco de Dados:** SQLite
- **Notificações:** SMTP

## Estrutura do Projeto

/desafios-conhecimento
│
├── main.py # Aplicação FastAPI
├── models.py # Modelos de dados
├── schemas.py # Esquemas para validação
├── services.py # Lógica de negócios
├── static/ # Arquivos estáticos (CSS, JS)
│ └── style.css
├── templates/ # Templates HTML Jinja2
│ ├── index.html
│ ├── challenge.html
│ └── profile.html
├── alembic/ # Scripts de migração 
│
├── requirements.txt # Dependências do projeto
└── README.md # Documentação do projeto

## Como Rodar o Projeto

1. Clone o Repositório:

    git clone <URL_DO_REPOSITÓRIO>
    cd knowledge-challenges
    python -m venv venv
    source venv/bin/activate 
    pip install -r requirements.txt

2. Configure o Banco de Dados:
    Configure as variáveis de ambiente para o banco de dados no arquivo .env.
3. Execute as Migrações do Banco de Dados:
    alembic upgrade head  # se usar SQLAlchemy

4. Inicie o Servidor:
    uvicorn main:app --reload

## Contribuindo
- Faça um fork deste repositório.
- Crie uma branch para sua feature ou correção (git checkout -b minha-feature).
- Faça commit das suas alterações (git commit -am 'Adiciona nova feature').
- Envie para o repositório remoto (git push origin minha-feature).
- Abra um pull request.
