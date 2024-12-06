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