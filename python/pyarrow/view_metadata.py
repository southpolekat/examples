#!/usr/bin/python

import sys
import pyarrow.parquet as pq

metadata = pq.read_metadata(sys.argv[1])

print "num_rows=%d" % metadata.num_rows
print "num_columns=%d" % metadata.num_columns

for i in range(metadata.row_group(0).num_columns):
    print " column %d: physical_type=%-10s   logical_type=%s" % (
            i,
            metadata.row_group(0).column(i).statistics.physical_type,
            metadata.row_group(0).column(i).statistics.logical_type) 
