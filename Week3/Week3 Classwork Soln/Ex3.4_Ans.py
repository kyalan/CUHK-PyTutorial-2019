import pandas as pd

df_movies = pd.read_csv('ml-latest-small/movies.csv')
df_ratings = pd.read_csv('ml-latest-small/ratings.csv')

movie_df = pd.DataFrame([{'Title': 'Deadpool', 'Distributor': 'Fox', 'Gross': 783.11},
                   {'Title': 'Captain America: Civil War', 'Distributor': 'Disney', 'Gross': 1153.30},
                   {'Title': 'Batman v Superman: Dawn of Justice', 'Distributor': 'Warner Bros.', 'Gross': 873.63}],
                  columns=['Title', 'Distributor', 'Gross']
                 )
movies = '|'.join(movie_df['Title'])

df_sub_movies = df_movies[df_movies['title'].str.contains(movies)]
df_sub = pd.merge(df_ratings, df_sub_movies, how='inner', left_on='movieId', right_on='movieId')
df_sub['datetime'] = pd.to_datetime(df_sub['timestamp'], unit='s')
df_sub['year'] = df_sub['datetime'].dt.year
df_sub

# Using groupby, find no. of ratings in each year.
df.groupby('year').agg({'rating': {'avg': np.average, 'count': pd.Series.count}})