from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from prisma import Prisma

# Algoritmo final de recomendação de filmes para um usuário baseado nos que ele já avaliou
# Casos possíveis
# 1. Usuário avaliou menos de 5 filmes - Recomendar os mais populares
# 2. Usuário já avaliou mais de 5 filmes - Recomendar filmes baseado no conteúdo do 