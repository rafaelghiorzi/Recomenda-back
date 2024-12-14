# movie-content-based.py

"""This algorithm is a content-based recommendation system 
that recommends movies similar to a given movie based on their genres."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from prisma import Prisma
import numpy as np

async def recommend_similar_movies(movie_id: int, limit: int = 10):
    db = Prisma()
    await db.connect()

    # Buscar todos os filmes
    movies = await db.movie.find_many()
    await db.disconnect()

    # Criar lista de gêneros para cada filme
    genres_list = [" ".join(movie.genres) for movie in movies]

    # Transformar gêneros em matriz TF-IDF
    vectorizer = TfidfVectorizer()
    genre_matrix = vectorizer.fit_transform(genres_list)

    # Identificar o índice do filme avaliado
    movie_index = next(i for i, m in enumerate(movies) if m.id == movie_id)

    # Calcular similaridade com todos os outros filmes
    similarities = cosine_similarity(genre_matrix[movie_index], genre_matrix).flatten()

    # Ordenar filmes por similaridade, excluindo o filme avaliado
    similar_indices = similarities.argsort()[-(limit + 1):-1][::-1]

    # Retornar os filmes similares
    similar_movies = [movies[i] for i in similar_indices]
    return similar_movies

# Exemplo de uso
import asyncio

async def main():
    movie_id = 1  # ID do filme que foi avaliado
    recommended_movies = await recommend_similar_movies(movie_id)
    for movie in recommended_movies:
        print(movie.title)

asyncio.run(main())
