#!/bin/bash

for file in *.csv
do
python proto_series.py $file
done
