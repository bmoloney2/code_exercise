#!/usr/bin/python

import csv
from prettytable import PrettyTable
from prettytable import from_csv
from prettytable import PLAIN_COLUMNS
from pprint import pprint
import itertools

filename = raw_input('Enter path to schedule: ')

#import csv to list and remove underscores
csv_list = []
with open(filename, 'r') as f:
    for line in f.readlines():
        z = line.replace('_', ' ')
	l = z.strip().split(',')
	csv_list.append((l))
    
#remove duplicates from list      
def unique(lst):
    last = object()
    for item in lst:
        if item == last:
            continue
        yield item
        last = item

#sort list and call unique to remove duplicates
def sort_and_unique(l):
    return list(unique(sorted(l, reverse=True)))
csv_su = sort_and_unique(csv_list)

pprint(csv_su)
