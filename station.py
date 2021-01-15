# PART 1
# TO DO:
# retrieve station code
import csv
with open('stations.csv', 'r') as stationcodes_file:
    stationcodes_reader = csv.reader(stationcodes_file)
    for line in stationcodes_reader:
        print(line)

# import the file
import json
with open('precipitation.json') as json_file:
    station_data = json.load(json_file)

# create empty list with 
valuesjanuary = list()
valuesfebruary = list()
valuesmarch = list()
valuesapril = list()
valuesmay = list()
valuesjune = list()
valuesjuly = list()
valuesaugust = list()
valuesseptember = list()
valuesoctober = list()
valuesnovember = list()
valuesdecember = list()

# select for station number and date
for station in station_data:
    station['value'] = str(station['value'])
    if station['station'] == 'GHCND:US1WAKG0038':
        year, month, day = station['date'].split('-')
        if month == '01':
            valuesjanuary.append(int(station['value']))
            sumjanuary = sum(valuesjanuary)
        if month == '02':
            valuesfebruary.append(int(station['value']))
            sumfebruary = sum(valuesfebruary)
        if month == '03':
            valuesmarch.append(int(station['value']))
            summarch = sum(valuesmarch)
        if month == '04':
            valuesapril.append(int(station['value']))
            sumapril = sum(valuesapril)
        if month == '05':
            valuesmay.append(int(station['value']))
            summay = sum(valuesmay)
        if month == '06':
            valuesjune.append(int(station['value']))
            sumjune = sum(valuesjune)
        if month == '07':
            valuesjuly.append(int(station['value']))
            sumjuly = sum(valuesjuly)
        if month == '08':
            valuesaugust.append(int(station['value']))
            sumaugust = sum(valuesaugust)
        if month == '09':
            valuesseptember.append(int(station['value']))
            sumseptember = sum(valuesseptember)
        if month == '10':
            valuesoctober.append(int(station['value']))
            sumoctober = sum(valuesoctober)
        if month == '04':
            valuesnovember.append(int(station['value']))
            sumnovember = sum(valuesnovember)
        if month == '12':
            valuesdecember.append(int(station['value']))
            sumdecember = sum(valuesdecember)

# Create list for sums
summonths = [sumjanuary, sumfebruary, summarch, sumapril, summay, sumjune, sumjuly, sumaugust, sumseptember, sumoctober, sumnovember, sumdecember]

# Convert list to json file
with open('json_summonths', 'w') as json_file_summonths:
    json.dump(summonths, json_file_summonths)

# PART 2
sumyear = sumjanuary + sumfebruary + summarch + sumapril + summay + sumjune + sumjuly + sumaugust + sumseptember + sumoctober + sumnovember + sumdecember
print(sumyear)

# calculate relative precipitation per month
perc_year = list()
for month in summonths:
    perc_year.append((int(month)/sumyear)*100)



