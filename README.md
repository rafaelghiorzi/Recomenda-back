project/
├── app/
│   ├── api/               # Rotas do FastAPI
│   │   ├── routes/        # Sub-rotas (filmes, usuários, etc.)
│   │   ├── __init__.py
│   ├── core/              # Configurações (DB, Auth, etc.)
│   ├── models/            # Definições dos modelos
│   ├── services/          # Algoritmos de recomendação e lógica
│   ├── schemas/           # Schemas do Pydantic para validação
│   └── __init__.py
├── prisma/                # Schema do Prisma
├── datasets/              # Arquivos do MovieLens
├── tests/                 # Testes do back-end
├── requirements.txt       # Dependências do projeto
├── README.md
└── main.py                # Entrada do FastAPI

To-do:
1.  Criar todas as rotas certinho (crud completo básico para cada rota) ✅
2. Criar uma autenticação Oauth2 para os usuários (rota signin e signup) ✅
3. Inserir os dados dos dataframes no banco de dados
4. começar a estruturar os algoritmos de recomendação