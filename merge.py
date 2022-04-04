from email import header
import pandas as pd
import csv

from wsproto import Headers
dataset1=[]
dataset2=[]
with open('dataset_1.csv','r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset1.append(row)
with open('dataset_2_sorted.csv','r') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        dataset2.append(row)
header1=dataset1[0]
planetdata1=dataset1[1:]
header2=dataset2[0]
planetdata2=dataset2[1:]
Headers=header1+header2
planetdata=[]
for index,data_row in enumerate(planetdata1):
    planetdata.append(planetdata1[index]+planetdata2[index])
with open('final.csv','a+',newline='') as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(Headers)
    csvwriter.writerows(planetdata)