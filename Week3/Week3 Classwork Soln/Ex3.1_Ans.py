# Obtain a fanfare record dataset with Business Cabin and price after tax over $10000.

df[(df['Cabin'] == 'Business') & (df['Price_tax'] > 10000)]