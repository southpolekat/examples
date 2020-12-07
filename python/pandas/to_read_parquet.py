#!/usr/bin/python

import pandas as pd

df = pd.DataFrame(data={
    'i':[1,2],
    't':['a','b'],
    'f':[0.1, 0.2]
    })
df.to_parquet('/tmp/test.parquet')
df2 = pd.read_parquet('/tmp/test.parquet')

print df
print df2
