#!/usr/bin/python

import sys
import pyarrow.parquet as pq

par = pq.ParquetFile(sys.argv[1])

print(par.metadata)
print(par.schema)

for c in range(par.metadata.num_columns):
    print(par.metadata.schema.column(c))
