# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 23:42:47 2019

@author: KY
"""

from urllib.request import urlopen
from urllib.parse import urlencode
import json

serviceurl = "https://sps-opendata.pilotsmartke.gov.hk/rest/getCarparkVacancies"
params = {}
params['carparkTypes'] = 'multi-storey'
params['vehicleTypes'] = 'privateCar'
url = serviceurl + '?' + urlencode(params)

output = urlopen(url).read()
print('Retrieved', len(output), 'characters')
outjson = json.loads(output)

#Discovering outjson
print(outjson['results'][0])

import pandas as pd
df = pd.DataFrame(outjson['results'])
print(df.head())
print(df.columns)

from pandas.io.json import json_normalize
df = json_normalize(outjson['results'])
print(df.head())
print(df.columns)

