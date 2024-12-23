# Sistema de Recomendação de Filmes

Bem-vindo ao **Recomenda Filme**, um sistema de back-end desenvolvido em Python utilizando o framework FastAPI. Este projeto foi criado com o objetivo de estudar e implementar algoritmos de recomendação, bem como explorar os fundamentos de Machine Learning no contexto de sistemas de recomendação de filmes.

## Funcionalidades do Projeto

O sistema conta com as seguintes funcionalidades principais:

1. **Recomendação Baseada em Conteúdo**: Sugere filmes semelhantes a um filme que o usuário acabou de avaliar, utilizando informações como gêneros e descrições.

2. **Recomendação Baseada em Avaliações Pessoais**: Gera sugestões com base nas avaliações feitas pelo usuário, destacando filmes alinhados às preferências expressas por ele.

3. **Recomendação Colaborativa**: Indica filmes populares entre usuários que possuem preferências similares ao usuário logado.

4. **Ranking dos Mais Bem Avaliados**: Exibe os filmes mais populares, baseando-se em médias ponderadas de avaliações e quantidade de votos.

## Dados e Armazenamento

Os dados utilizados no sistema são provenientes dos **small datasets do MovieLens**. Esses datasets incluem informações sobre filmes, avaliações, gêneros e tags, e são armazenados em um banco de dados PostgreSQL, gerenciado pela biblioteca **Prisma**.

## Tecnologias Utilizadas

### Linguagens e Frameworks

- **Python 3.10+**
- **FastAPI** (para criação do back-end)
- **Prisma** (para ORM e gerenciamento de banco de dados relacional)

### Banco de Dados

- **PostgreSQL**

### Bibliotecas de Machine Learning e Processamento de Dados

- **Pandas**
- **NumPy**
- **scikit-learn**
- **TF-IDF Vectorizer**

### Autenticação

- **OAuth2** com suporte a tokens de acesso e refresh tokens, utilizando o padrão **JWT** para segurança.

## Estrutura do Projeto

A estrutura do projeto segue um padrão modular e escalável:

```
project/
├── app/
│   ├── api/               # Rotas do FastAPI
│   │   ├── routes/        # Sub-rotas (filmes, usuários, etc.)
│   │   ├── __init__.py
│   ├── core/              # Configurações (DB, Auth, etc.)
│   ├── models/            # Definições dos modelos
│   ├── services/          # Algoritmos de recomendação e lógica
│   ├── schemas/           # Schemas do Pydantic para validação
│   └── __init__.py
├── prisma/                # Schema do Prisma
├── datasets/              # Arquivos do MovieLens
├── tests/                 # Testes do back-end
├── requirements.txt       # Dependências do projeto
├── README.md
└── main.py                # Entrada do FastAPI
```

## Configuração do Ambiente

### Requisitos

Certifique-se de ter instalado:

- Python 3.10+
- PostgreSQL

### Instalação

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/recomenda-filme.git
   cd recomenda-filme
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente no arquivo `.env`:

   ```env
   DATABASE_URL=postgresql://usuario:senha@localhost:5432/seu_banco
   SECRET_KEY=sua_chave_secreta
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

5. Execute as migrações do Prisma para criar as tabelas no banco de dados:

   ```bash
   prisma migrate deploy
   ```

6. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```

### Acessando o Sistema

- Documentação das APIs (Swagger): `http://localhost:8000/docs`
- Redoc: `http://localhost:8000/redoc`

Desenvolvido por Rafael Dias Ghiorzi .
