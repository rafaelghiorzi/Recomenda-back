# colaborative.py

"""This algorithm is a collaborative filtering recommendation system that recommends
movies to a user based on the ratings of similar users."""

import pandas as pd
from prisma import Prisma

async def collaborative_filtering_recommendation(user_id: int, limit: int = 10):
    db = Prisma()
    await db.connect()

    # Buscar todas as avaliações
    ratings = await db.rating.find_many()
    flattened = [rating.model_dump() for rating in ratings]
    ratings_df = pd.DataFrame(flattened).drop(columns=['user', 'movie']).set_index('id')

    # Criar matriz usuário-filme
    user_movie_matrix = ratings_df.pivot_table(
        index='userId', 
        columns='movieId', 
        values='score'
    ).fillna(0)

    # Calcular similaridade entre usuários
    from sklearn.metrics.pairwise import cosine_similarity
    user_similarity = cosine_similarity(user_movie_matrix)

    # Identificar usuários mais similares
    user_index = user_movie_matrix.index.get_loc(user_id)
    similar_users = user_similarity[user_index].argsort()[:-1][::-1]

    # Filmes já avaliados pelo usuário
    user_rated_movies = user_movie_matrix.loc[user_id]
    already_rated = user_rated_movies[user_rated_movies > 0].index

    # Recomendação baseada nos usuários similares
    similar_user_ratings = user_movie_matrix.iloc[similar_users].mean(axis=0)
    similar_user_ratings = similar_user_ratings.drop(already_rated, errors='ignore')
    recommended_movies = similar_user_ratings.sort_values(ascending=False).head(limit)

    await db.disconnect()
    return recommended_movies.index.tolist()

# Executar o algoritmo
import asyncio

async def main():
    moviesIds = await collaborative_filtering_recommendation(68)
    db = Prisma()
    await db.connect()
    for movieId in moviesIds:
        movie = await db.movie.find_unique(where={'id': movieId})
        if movie:
            print(movie.title)
    await db.disconnect()

asyncio.run(main())