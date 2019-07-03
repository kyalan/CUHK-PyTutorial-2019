# Q.1
# Create a Series object: Airline names, with IATA code as index 
# KA = Cathay Dragon ; BR = Eva Air ; JL = Japan Airlies ; KE = Korean Air


# Q.2
# What is the price ratio between Ben's ticket and Tony's ticket ?
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