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
3. Inserir os dados dos dataframes no banco de dados ✅
4. começar a estruturar os algoritmos de recomendação ✅


## **1. Baseado em Popularidade**
### **Como funciona:**
- Esse algoritmo é simples e não considera o histórico do usuário. Ele recomenda os filmes com base em métricas gerais como:
  - **`avgRating`**: Média das notas de um filme.
  - **`ratingCount`**: Número total de avaliações de um filme.

### **Vantagens:**
- Fácil de implementar.
- Funciona para novos usuários (problema de cold start).
- Recomendação de filmes que são populares entre todos os usuários.

### **Desvantagens:**
- Não é personalizado.
- Filmes menos avaliados, mas com alta qualidade, podem não aparecer.

---

## **2. Filtragem Baseada em Conteúdo**
### **Como funciona:**
- Compara as características de itens (filmes) para recomendar itens similares a aqueles que o usuário já gostou.
- **Etapas principais:**
  1. **Extração de características:** Os atributos dos filmes, como gêneros ou tags, são processados.
  2. **Similaridade:** Calcula a similaridade entre filmes usando métricas como Cosine Similarity.
  3. **Recomendação:** Retorna filmes com características mais próximas dos filmes que o usuário avaliou positivamente.

### **Exemplo:**
Se um usuário avaliou bem um filme de comédia, ele pode receber recomendações de outros filmes de comédia com base nos gêneros ou tags.

### **Vantagens:**
- Boa para novos usuários com pouco histórico.
- Baseia-se apenas nos dados dos itens.

### **Desvantagens:**
- Requer bons metadados sobre os filmes.
- Não considera a colaboração entre usuários.

---

## **3. Filtragem Colaborativa**
### **Como funciona:**
Baseia-se no comportamento dos usuários. Há duas variações principais:
1. **User-User Collaborative Filtering:**
   - Compara usuários entre si.
   - Recomenda filmes que usuários semelhantes gostaram.
   - Exemplo: "Usuários como você gostaram de X".

2. **Item-Item Collaborative Filtering:**
   - Compara filmes entre si.
   - Recomenda filmes similares àqueles que o usuário já avaliou bem.
   - Exemplo: "Você gostou de Y, então talvez goste de X porque outros usuários que gostaram de Y também gostaram de X".

### **Etapas principais:**
1. **Criar uma matriz usuário-filme:** Cada linha representa um usuário, cada coluna representa um filme e o valor é a nota dada.
2. **Calcular similaridade:** Usa métricas como Cosine Similarity ou Correlação de Pearson para encontrar semelhanças.
3. **Recomendar:** Baseia-se nos filmes avaliados pelos usuários mais semelhantes.

### **Vantagens:**
- Não precisa de dados sobre os filmes, apenas interações usuário-filme.
- Altamente personalizável.

### **Desvantagens:**
- Problema de cold start para usuários ou filmes novos.
- Requer um grande número de avaliações para funcionar bem.

---

### **Comparação Geral**

| Algoritmo                | Personalização | Requer Dados de Filmes | Problema de Cold Start | Complexidade |
|--------------------------|----------------|-------------------------|-------------------------|--------------|
| Popularidade             | Baixa          | Não                    | Sim                    | Baixa        |
| Baseado em Conteúdo      | Média          | Sim                    | Parcial                | Média        |
| Filtragem Colaborativa   | Alta           | Não                    | Sim                    | Média        |
| Fatoração de Matrizes    | Alta           | Não                    | Sim                    | Alta         |
