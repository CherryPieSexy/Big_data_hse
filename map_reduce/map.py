#!/usr/bin/env python
# coding=utf-8
import sys

for line in sys.stdin:
    line = line.split(',')
    print(line[0] + '\t' + line[1] + '\t' + line[10] + '\t' + line[11])
