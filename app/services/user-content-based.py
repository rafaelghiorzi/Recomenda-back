# user-content-based.py

"""This algorithm is a content-based recommendation system that recommends
movies to a user based on the genres of movies they have previously rated highly."""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from prisma import Prisma

async def recommend_movies_based_on_genre(user_id: int, limit: int = 10):
    db = Prisma()
    await db.connect()

    # Buscar todos os filmes
    movies = await db.movie.find_many()
    # Buscar as avaliações do usuário
    ratings = await db.rating.find_many(where={"userId": user_id})
    await db.disconnect()

    # Filmes avaliados pelo usuário e suas notas
    user_ratings = {rating.movieId: rating.score for rating in ratings}

    # Criar matriz TF-IDF para gêneros
    genres_list = [" ".join(movie.genres) for movie in movies]
    vectorizer = TfidfVectorizer()
    genre_matrix = vectorizer.fit_transform(genres_list)

    # Identificar filmes bem avaliados pelo usuário
    liked_movie_ids = [movie_id for movie_id, score in user_ratings.items() if score >= 4]
    if not liked_movie_ids:
        return []

    # Calcular similaridade com os filmes bem avaliados
    liked_indices = [i for i, m in enumerate(movies) if m.id in liked_movie_ids]
    user_profile = genre_matrix[liked_indices].mean(axis=0)
    user_profile = np.asarray(user_profile)  # Convert to numpy array
    similarities = cosine_similarity(user_profile, genre_matrix).flatten()

    # Ordenar os filmes baseando-se na similaridade
    similar_indices = similarities.argsort()[::-1]

    # Excluir filmes já avaliados
    already_rated = set(user_ratings.keys())
    recommended_movies = [
        movies[i] for i in similar_indices if movies[i].id not in already_rated
    ][:limit]

    return recommended_movies

# Executar a recomendação
import asyncio
movies = asyncio.run(recommend_movies_based_on_genre(1))
for movie in movies:
    print(movie.title)