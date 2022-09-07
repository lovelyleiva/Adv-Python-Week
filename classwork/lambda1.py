# import csv

# policeFile = open('911.csv', 'r')
# reader = csv.DictReader(policeFile)
# policeList = list()
# for dictionary in reader:
#     policeList.append(dictionary)

# missingFilter = list(filter(lambda x: x['zip_code'] != 0 or x['neighborhood'] != '' or x['totalresponsetime'] != '', policeList ))

# from functools import reduce 

# AvgTotalResponseTime = reduce(lambda num1, num2: (float(num1) + float(num2['totalresponsetime'])), missingFilter, 0.0)
# print(AvgTotalResponseTime/len(missingFilter))

# ResponsetimeList = []
# for i in range(0,len(missingFilter)):
#     if missingFilter[i]['totalresponsetime'] != '':
#         ResponsetimeList.append(float(missingFilter[i]['totalresponsetime']))

# AvgTotalResponseTime = reduce(lambda x,y: x+ y,ResponsetimeList)
# print(AvgTotalResponseTime/len(missingFilter))
#AvgDispatchTime

#AvgTotalTime


import csv
from functools import reduce
f = open('911.csv', "r")
policeList = list(csv.DictReader(f))
missingFilter = list(filter(lambda x: x['zip_code'] != 0 and x['neighborhood'] != '' and x['totalresponsetime'] != '', policeList ))
missingFilter = list(filter(lambda x: x['totalresponsetime'] != '', missingFilter))
AvgTotalResponseTime = reduce(lambda num1, num2: (float(num1) + float(num2['totalresponsetime'])), missingFilter, 0.0)
print(AvgTotalResponseTime/len(missingFilter))