# Subset DataFrame
import pandas as pd

ticket_1 = pd.Series({'Name': 'Ben',
                        'Destination': 'Maldives',
                        'Price': 14610.0})
ticket_2 = pd.Series({'Name': 'Julian',
                        'Destination': 'San Francisco',
                        'Price': 3480.0})
ticket_3 = pd.Series({'Name': 'Tony',
                        'Destination': 'Shanghai',
                        'Price': 880.00})
df = pd.DataFrame([ticket_1, ticket_2, ticket_3])
df.head()

# transpose
df.T
df.T.loc['Price']
# deleting row
copy_df = df.copy()
copy_df = copy_df.drop(1)
copy_df
# deleting column
del copy_df['Name']
copy_df
# add a column
df['Flight Date'] = None
df

# read csv (with chunk)
import os
os.chdir('M:/Student/Python_tutorial/Week3-20190705T070151Z-001/Week3 - 2019')

zipfile = 'train.csv.zip'
df = pd.read_csv(zipfile, compression='zip')
df.head()
df.shape
print(df.memory_usage().sum()/1024**2, 'MB')

df_chunk = pd.read_csv(zipfile, compression='zip',chunksize=1024)
i = 0
for df in df_chunk:
    i += 1
    print(df.head())
    print(df.shape)
    print(df.memory_usage().sum()/1024**2, 'MB')
    if i > 4: break

# DataFrame info
df = pd.read_csv('fanfares_2018.csv')
df.head()
df.tail()
df.describe()
df.info()
dir(df)

df.columns
df.rename(columns={'Date_start':'UseDuration_Start'
                  , 'Date_end':'UseDuration_End'
                  }, inplace=True)
df.head()

# Querying DataFrame
df['Cabin'] == 'Business'
# direct filtered
only_business = df[df['Cabin'] == 'Business']
only_business.head()
# filtered and fill with NA
only_business = df.where(df['Cabin'] == 'Business')
only_business.head()
only_business['Cabin'].count()
only_business = only_business.dropna()
only_business.head()

df_filtered = df[(df['Cabin'] == 'Business') | (df['Price_tax'] > 4000)]
len(df_filtered)
df_filtered.count()

#################################
# Exercise 3.1
###################################

# Sorting DataFrame
df_filtered.sort_values(['Price_tax'])
df_filtered.sort_values(['Price_tax'], ascending=False)
df_filtered.sort_values(['Price_tax', 'Date_start'], ascending=[False, True])

# Missing Values Handling
df = pd.read_csv('fanfares_2018.csv', parse_dates=['Date_start', 'Date_end'])
df_tpe = df[df['Destination']=='Taipei']
df_tpe
df_tpe = df_tpe.sort_values(['Date_start'])
df_tpe

df_tpe.isna()
df_tpe.dropna()
df_tpe.fillna(method='bfill')
df_tpe.fillna(method='ffill')

#################################
# Exercise 3.2
###################################

# Merging
Gross_df = pd.DataFrame([{'Title': 'Deadpool', 'Gross': 783.11},
                         {'Title': 'Captain America', 'Gross': 1153.30},
                         {'Title': 'Ip Man 3', 'Gross': 156.13}])
Distributor_df = pd.DataFrame([{'Title': 'Deadpool', 'Distributor': 'Fox'},
                         {'Title': 'Captain America', 'Distributor': 'Disney'},
                         {'Title': '踏血尋梅', 'Distributor': '美亞'}])
print(Gross_df.head())
print(Distributor_df.head())

Gross_df = Gross_df.set_index('Title')
Distributor_df = Distributor_df.set_index('Title')
pd.merge(Gross_df, Distributor_df, how='outer', left_index=True, right_index=True)
pd.merge(Gross_df, Distributor_df, how='inner', left_index=True, right_index=True)
pd.merge(Gross_df, Distributor_df, how='left', left_index=True, right_index=True)
pd.merge(Gross_df, Distributor_df, how='right', left_index=True, right_index=True)
Gross_df = Gross_df.reset_index()
Distributor_df = Distributor_df.reset_index()

pd.merge(Gross_df, Distributor_df, how='left', left_on='Title', right_on='Title')

#################################
# Exercise 3.3
###################################

import pandas as pd
import numpy as np

import os
os.chdir('C:/Users/KY/Google Drive/CUHKPyTutorial2019/Week3')

df_movies = pd.read_csv('ml-latest-small/movies.csv')
df_ratings = pd.read_csv('ml-latest-small/ratings.csv')
df = pd.merge(df_ratings, df_movies, how='inner', left_on='movieId', right_on='movieId')
df.info()

# Finding average with filtering each title
for title in df['title'].unique():
    avg = np.average(df.where(df['title']==title).dropna()['rating'])
    print('Movie ' + title + ' have an average rating of ' + str(avg))
# Group by
for title, frame in df.groupby('title'):
    avg = np.average(frame['rating'])
    print('Movie ' + title + ' have an average rating of ' + str(avg))
# Group by (1 sentence)
df.groupby('title').agg({'rating': np.average})

pd.set_option('max_rows', 10)

df.groupby('title')['rating'].agg({'avg': np.average, 'sum': np.sum})
df.groupby('title')['rating', 'timestamp'].agg({'max': np.max, 'min': np.min})

#################################
# Exercise 3.4
###################################

# Categorical Variables
df.genres.head()
df.genres.memory_usage()
df.genres.value_counts()
cat_genres = pd.Categorical(df.genres)
cat_genres
cat_genres.memory_usage()

# Pivot Tables
import pandas as pd
import numpy as np

df_movies = pd.read_csv('ml-latest-small/movies.csv')
df_ratings = pd.read_csv('ml-latest-small/ratings.csv')

df = pd.merge(df_ratings, df_movies, how='inner', left_on='movieId', right_on='movieId')
df['datetime'] = pd.to_datetime(df['timestamp'], unit='s')
df['weekday'] = df['datetime'].dt.weekday

df.head()

df[df['datetime'].dt.year>2010] \
    .pivot_table(values='rating', index='title', columns='weekday', aggfunc=np.mean) \
    .dropna()
df[df['datetime'].dt.year>2010] \
    .pivot_table(values='rating', index='title', columns='weekday', aggfunc=np.mean, margins=True) \
    .dropna()
    
#################################
# Exercise 3.5
###################################
    
# Numpy
import numpy as np

# array creation
np.array([4, 5, 6])
np.array([[7, 8, 9], [10, 11, 12]])    
# array dimension
m = np.array([[7, 8, 9], [10, 11, 12]])    
m.shape
# sequence
n = np.arange(0, 30, 2) # start at 0 count up by 2, stop before 30
n
# reshape the array / matrix
n = n.reshape(3, 5) # reshape array to be 3x5
n.resize(3, 5) # in-place
n
# interpolation
o = np.linspace(0, 4, 9) # return 9 evenly spaced values from 0 to 4
o

# 1-matrix
np.ones([3, 2])
np.ones([3,2,2])
# 0-matrix
np.zeros([2, 3])
# identity matrix
np.eye(3)
# diagonalization / get diagonal
y = np.diag([1, 2, 3, 4])
np.diag(y)
# repeat arrays
np.array([1, 2, 3] * 3)
np.repeat([1, 2, 3], 3)

# combining arrays
p = np.ones([2, 3])
np.vstack([p, 2*p])
np.hstack([p, 2*p])

# arithmetics (element-wise)
x = np.array([1,2,3])
y = np.array([4,5,6])
print(x+y, x-y, x*y, x/y, x**2)

# Inner / Dot Product
x.dot(y)

# transpose
z = np.array([y, y**2])
z.shape
z.T
z.T.shape

# type of matrix
z.dtype
z.astype('f')

# Math functions
a = np.array([-4, -2, 1, 3, 5])
print(a.sum(), a.max(), a.min(), a.mean(), a.std(), a.argmax(), a.argmin())

# Slicing
# Array
s = np.arange(13)**2
s[0], s[4], s[-1], s[1:5], s[-4:]
s[-5::-2] # array[start:stop:stepsize]

# Matrix
r = np.arange(36)
r.resize((6, 6))
r
r[2, 2], r[3, 3:6], r[:2, :-1], r[-1, ::2], r[r > 30]
r[r > 30] = 30
r

#################################
# Exercise 3.6
###################################

#################################
# Assignment 3
###################################