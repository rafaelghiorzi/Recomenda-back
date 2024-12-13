from prisma import Prisma

async def get_popular_movies(limit: int = 10, min_votes: int = 10):
    db = Prisma()
    await db.connect()
    
    # Filmes com maior número de avaliações
    movies = await db.movie.find_many()
    
    mediaGeral = sum(movie.avgRating for movie in movies) / len(movies)
    
    # filtrar filmes com menos de 10 avaliações
    movies = [movie for movie in movies if movie.ratingCount > min_votes]
    
    # calcular a média ponderada para cada filme
    def calculateWR(movie):
        v = movie.ratingCount
        r = movie.avgRating
        return ( (v * r) + (min_votes * mediaGeral) ) / (v + min_votes)
    
    # ordenar os filmes por média ponderada e limitar a quantidade filmes
    movies.sort(key=calculateWR, reverse=True)
    popularMovies = movies[:limit]

    await db.disconnect()
    return popularMovies

# Executar a função
import asyncio
movies = asyncio.run(get_popular_movies())
for movie in movies:
    print(movie.title)