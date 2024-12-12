import pandas as pd
from prisma import Prisma
import asyncio

# Ler os CSVs
movies_df = pd.read_csv("dataframes/movies.csv")
ratings_df = pd.read_csv("dataframes/ratings.csv")
tags_df = pd.read_csv("dataframes/tags.csv")

moviesSummary = ratings_df.groupby('movieId').agg(
    avgRating =('rating', 'mean'),
    numRatings = ('rating', 'count')
).reset_index()

print(moviesSummary.head())

async def movies():
    prisma = Prisma()
    await prisma.connect()
    
    movies = movies_df.to_dict(orient="records")
    
    for movie in movies:
        genres = movie['genres'].split("|") if "genres" in movie else []
        await prisma.movie.create(
            data={
                "id": int(movie['movieId']),
                "title": movie['title'],
                "genres": genres
            }
        )
        
    await prisma.disconnect()
    print("Movies inserted")
    
async def updateMovies():
    prisma = Prisma()
    await prisma.connect()
    
    data = moviesSummary.to_dict(orient="records")
    
    for movie in data:
        await prisma.movie.update(
            where={
                "id": int(movie['movieId'])
            },
            data={
                "avgRating": float(movie['avgRating']),
                "ratingCount": int(movie['numRatings'])
            }
        )
        
    await prisma.disconnect()
    print("Movies updated")

async def ratings():
    prisma = Prisma()
    await prisma.connect()
    
    ratings = ratings_df.to_dict(orient="records")
    
    for rating in ratings:
        await prisma.rating.create(
            data={
                "userId": int(rating['userId']),
                "movieId": int(rating['movieId']),
                "score": float(rating['rating']),
                "createdAt": pd.to_datetime(rating['timestamp'], unit='s')
            }
        )
        
    await prisma.disconnect()
    print("Ratings inserted")
    
async def tags():
    prisma = Prisma()
    await prisma.connect()
    
    tags = tags_df.to_dict(orient="records")
    
    for tag in tags:
        await prisma.tag.create(
            data={
            "userId": int(tag['userId']),
            "movieId": int(tag['movieId']),
            "tag": tag['tag'],
            "createdAt": pd.to_datetime(tag['timestamp'], unit='s')
            }
        )
        
    await prisma.disconnect()
    print("Tags inserted")
    
async def users():
    prisma = Prisma()
    await prisma.connect()
    
    # create example users from 0 to 600
    for i in range(0,600):
        await prisma.user.create(
            data={
                "id": i,
                "username" : f'user{i}',
                "email" : f'user{i}@gmail.com',
                'password' : '12345',
            }
        )
    
    await prisma.disconnect()
    print("Users inserted")
        
asyncio.run(updateMovies()) # run any of the above functions here if needeed

