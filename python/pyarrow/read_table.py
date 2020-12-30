#!/usr/bin/python

import sys
import pyarrow.parquet as pq

table = pq.read_table(sys.argv[1])
print(table.to_pandas())
