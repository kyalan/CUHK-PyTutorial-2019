import csv
import os 

#wkdir = 'C:/Users/KY/Google Drive/CUHKPyTutorial2019/Week2'
wkdir = 'C:/Users/KY/Google Drive/CUHKPyTutorial2019/Week2'
if os.getcwd()!=wkdir:
    os.chdir(wkdir)

csvfile = open('fanfares.csv')
dataset = csv.reader(csvfile, delimiter=',', quotechar='"')
[' '.join(row) for row in dataset]
    