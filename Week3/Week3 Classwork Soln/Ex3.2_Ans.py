# Discover any missing values insides
df = pd.read_csv('fanfares_2018.csv', parse_dates=['Date_start', 'Date_end'])
print(df.info())

# indicate the rows having missing values
df[df.isna()]

# fill the missing values according to the offers in the same city with appropriate methods
df = df.sort_values(['Destination', 'Date_start'])
df = df.fillna(method='ffill')
df.info()
df[df.Destination=='Copenhagen']