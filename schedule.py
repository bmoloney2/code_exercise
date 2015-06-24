#!/usr/bin/python

import csv,os
import pandas as pd

filename = raw_input('Enter path to schedule: ')

#import header and remove underscores/commas
csv_header = []
def pull_headers(l):
   with open(l) as f:
      reader = f.xreadlines()
      row1 = next(reader)
      no_undr = row1.replace('_', ' ')
      no_comm = no_undr.replace(',', ' ')
      csv_header.append(no_comm)
      return csv_header

#import csv to list
csv_list = []
with open(filename, 'r') as f:
   f.readline()
   for line in f.readlines():
	 l = line.strip().split(',')
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
   return list(unique(sorted(l)))

#get data from functions and sort list for printing
csv_clnheader = (pull_headers(filename))
csv_clean = (sort_and_unique(csv_list))
csvlst_srt = sorted(csv_clean, key = lambda x : (x[2])) #sort list by run number

#clear screen and print header/table
os.system('clear')
for items in csv_clnheader:
    print (''.join(map(str, items)))
df = pd.DataFrame(csvlst_srt)
print df
