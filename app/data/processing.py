import pandas as pd
import asyncio
from prisma import Prisma

# Função para converter resultados do Prisma em uma lista de dicionários
def flatten_prisma_results(data):
    """
    Converte o resultado do Prisma para uma lista de dicionários utilizáveis pelo pandas.
    """
    return [dict(item) for item in data]

# Função para carregar dados de uma tabela e ignorar colunas relacionadas
async def load_table_data(model, ignore_columns=None):
    """
    Carrega os dados de um modelo Prisma e retorna um DataFrame pandas sem colunas relacionadas.
    
    Parameters:
        - model: Método Prisma correspondente ao modelo (e.g., client.movie.find_many)
        - ignore_columns: Lista de colunas a serem ignoradas no DataFrame.
    
    Returns:
        - DataFrame com os dados do modelo.
    """
    data = await model()
    df = pd.DataFrame(flatten_prisma_results(data))
    if ignore_columns:
        df = df.drop(columns=ignore_columns, errors="ignore")
    return df

# Função principal assíncrona
async def main():
    # Inicializar o cliente Prisma
    client = Prisma()
    await client.connect()

    try:
        # Carregar os dados das tabelas, ignorando colunas relacionadas
        movies_df = await load_table_data(client.movie.find_many, ignore_columns=["tags", "ratings", "genome"])
        ratings_df = await load_table_data(client.rating.find_many, ignore_columns=["user", "movie"])
        tags_df = await load_table_data(client.tag.find_many, ignore_columns=["user", "movie"])
        users_df = await load_table_data(client.user.find_many, ignore_columns=["tags", "ratings"])

        # Inspecionar os DataFrames
        print("Movies DataFrame")
        print(movies_df.head(), "\n")

        print("Ratings DataFrame")
        print(ratings_df.head(), "\n")

        print("Tags DataFrame")
        print(tags_df.head(), "\n")

        print("Users DataFrame")
        print(users_df.head(), "\n")

    finally:
        # Finalizar conexão Prisma
        await client.disconnect()