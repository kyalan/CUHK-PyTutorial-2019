# Discover any missing values insides
df = pd.read_csv('fanfares_2018.csv', parse_dates=['Date_start', 'Date_end'])

# indicate the rows having missing values


# fill the missing values according to the offers in the same city with appropriate methods