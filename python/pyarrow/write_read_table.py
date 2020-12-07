#!/usr/bin/python

import pandas as pd
import pyarrow as pa

df = pd.DataFrame(data={
        'i':[1,2],
        't':['a','b'],
        'f':[0.1, 0.2]
        })
table = pa.Table.from_pandas(df)

import pyarrow.parquet as pq

pq.write_table(table, '/tmp/test.parquet')  

table2=pq.read_table('/tmp/test.parquet')

print table.to_pandas()
print table2.to_pandas()
