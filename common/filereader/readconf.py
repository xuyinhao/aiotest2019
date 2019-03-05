import csv
serverconf = csv.reader(open('server.csv'),'r')
for confv in serverconf:
    print(confv)
