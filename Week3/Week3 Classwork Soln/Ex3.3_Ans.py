import pandas as pd

df_movies = pd.read_csv('ml-latest-small/movies.csv')
df_ratings = pd.read_csv('ml-latest-small/ratings.csv')
print(df_movies.info())
print(df_ratings.info())

movies = '|'.join(movie_df['Title'])

# Please filter df_movies having the movies, 
# ['Deadpool', 'Captain America: Civil War', 'Batman v Superman: Dawn of Justice']
# and merge with df_ratings...
df_sub_movies = df_movies[df_movies['title'].str.contains(movies)]
df_sub = pd.merge(df_ratings, df_sub_movies, how='inner', left_on='movieId', right_on='movieId')


df_sub # result