# PART 1
# import the file
import json
with open('precipitation.json') as json_file:
    station_data = json.load(json_file)

# Create empty dictionary
years_sum_months = {'january': [], 'february': [], 'march': [], 'april': [], 'may': [], 'june': [], 'july': [], 'august': [], 'september': [], 'october': [], 'november': [], 'december': []}

# Filter for station Seatte and for months and append
for station in station_data:
    station['value'] = str(station['value'])
    if station['station'] == 'GHCND:US1WAKG0038':
        year, month, day = station['date'].split('-')
        if month == '01':
                years_sum_months['january'].append(int(station['value']))
        if month == '02':
                years_sum_months['february'].append(int(station['value']))
        if month == '03':
                years_sum_months['march'].append(int(station['value']))
        if month == '04':
                years_sum_months['april'].append(int(station['value']))
        if month == '05':
                years_sum_months['may'].append(int(station['value']))
        if month == '06':
                years_sum_months['june'].append(int(station['value']))
        if month == '07':
                years_sum_months['july'].append(int(station['value']))
        if month == '08':
                years_sum_months['august'].append(int(station['value']))
        if month == '09':
                years_sum_months['september'].append(int(station['value']))
        if month == '10':
                years_sum_months['october'].append(int(station['value']))
        if month == '11':
                years_sum_months['november'].append(int(station['value']))
        if month == '12':
                years_sum_months['december'].append(int(station['value']))

# sum values for every month
for key in years_sum_months: 
    years_sum_months[key] = sum(years_sum_months[key])

# Convert dictionary to json file
with open('json_summonths_seattle', 'w') as json_file_summonths_seattle:
    json.dump(years_sum_months, json_file_summonths_seattle)

# PART 2: calculate sum for whole year
sumyear_seattle = sum(years_sum_months.values())

# calculate relative precipitation per month
perc_year = list()
for month in years_sum_months.values():
    perc_year.append((int(month)/sumyear_seattle)*100)
print(perc_year)

# PART 3
# Create empty dictionary
years_sum_months_cin = {'january': [], 'february': [], 'march': [], 'april': [], 'may': [], 'june': [], 'july': [], 'august': [], 'september': [], 'october': [], 'november': [], 'december': []}

# Filter for station Cincinatti and for months and append
for station in station_data:
    station['value'] = str(station['value'])
    if station['station'] == 'GHCND:USC00513317':
        year, month, day = station['date'].split('-')
        if month == '01':
                years_sum_months_cin['january'].append(int(station['value']))
        if month == '02':
                years_sum_months_cin['february'].append(int(station['value']))
        if month == '03':
                years_sum_months_cin['march'].append(int(station['value']))
        if month == '04':
                years_sum_months_cin['april'].append(int(station['value']))
        if month == '05':
                years_sum_months_cin['may'].append(int(station['value']))
        if month == '06':
                years_sum_months_cin['june'].append(int(station['value']))
        if month == '07':
                years_sum_months_cin['july'].append(int(station['value']))
        if month == '08':
                years_sum_months_cin['august'].append(int(station['value']))
        if month == '09':
                years_sum_months_cin['september'].append(int(station['value']))
        if month == '10':
                years_sum_months_cin['october'].append(int(station['value']))
        if month == '11':
                years_sum_months_cin['november'].append(int(station['value']))
        if month == '12':
                years_sum_months_cin['december'].append(int(station['value']))

# sum values for every month
for key in years_sum_months_cin: 
    years_sum_months_cin[key] = sum(years_sum_months_cin[key])

# Convert dictionary to json file
with open('json_summonths_cincinatti', 'w') as json_file_summonths_cincinatti:
    json.dump(years_sum_months_cin, json_file_summonths_cincinatti)

# calculate sum for whole year
sumyear_cincinatti = sum(years_sum_months_cin.values())

# calculate relative precipitation per month
perc_year_cin = list()
for month in years_sum_months_cin.values():
    perc_year_cin.append((int(month)/sumyear_cincinatti)*100)
print(perc_year_cin)

# Create empty dictionary
years_sum_months_maui = {'january': [], 'february': [], 'march': [], 'april': [], 'may': [], 'june': [], 'july': [], 'august': [], 'september': [], 'october': [], 'november': [], 'december': []}

# Filter for station Maui and for months and append
for station in station_data:
    station['value'] = str(station['value'])
    if station['station'] == 'GHCND:USW00093814':
        year, month, day = station['date'].split('-')
        if month == '01':
                years_sum_months_maui['january'].append(int(station['value']))
        if month == '02':
                years_sum_months_maui['february'].append(int(station['value']))
        if month == '03':
                years_sum_months_maui['march'].append(int(station['value']))
        if month == '04':
                years_sum_months_maui['april'].append(int(station['value']))
        if month == '05':
                years_sum_months_maui['may'].append(int(station['value']))
        if month == '06':
                years_sum_months_maui['june'].append(int(station['value']))
        if month == '07':
                years_sum_months_maui['july'].append(int(station['value']))
        if month == '08':
                years_sum_months_maui['august'].append(int(station['value']))
        if month == '09':
                years_sum_months_maui['september'].append(int(station['value']))
        if month == '10':
                years_sum_months_maui['october'].append(int(station['value']))
        if month == '11':
                years_sum_months_maui['november'].append(int(station['value']))
        if month == '12':
                years_sum_months_maui['december'].append(int(station['value']))

# sum for every month
for key in years_sum_months_maui: 
    years_sum_months_maui[key] = sum(years_sum_months_maui[key])

# Convert dictionary to json file
with open('json_summonths_maui', 'w') as json_file_summonths_maui:
    json.dump(years_sum_months_maui, json_file_summonths_maui)

# calculate sum for whole year
sumyear_maui = sum(years_sum_months_maui.values())

# calculate relative precipitation per month
perc_year_maui = list()
for month in years_sum_months_maui.values():
    perc_year_maui.append((int(month)/sumyear_maui)*100)
print(perc_year_maui)

# Create empty dictionary
years_sum_months_san = {'january': [], 'february': [], 'march': [], 'april': [], 'may': [], 'june': [], 'july': [], 'august': [], 'september': [], 'october': [], 'november': [], 'december': []}

# Filter for station San Diego and for months and append
for station in station_data:
    station['value'] = str(station['value'])
    if station['station'] == 'GHCND:US1CASD0032':
        year, month, day = station['date'].split('-')
        if month == '01':
                years_sum_months_san['january'].append(int(station['value']))
        if month == '02':
                years_sum_months_san['february'].append(int(station['value']))
        if month == '03':
                years_sum_months_san['march'].append(int(station['value']))
        if month == '04':
                years_sum_months_san['april'].append(int(station['value']))
        if month == '05':
                years_sum_months_san['may'].append(int(station['value']))
        if month == '06':
                years_sum_months_san['june'].append(int(station['value']))
        if month == '07':
                years_sum_months_san['july'].append(int(station['value']))
        if month == '08':
                years_sum_months_san['august'].append(int(station['value']))
        if month == '09':
                years_sum_months_san['september'].append(int(station['value']))
        if month == '10':
                years_sum_months_san['october'].append(int(station['value']))
        if month == '11':
                years_sum_months_san['november'].append(int(station['value']))
        if month == '12':
                years_sum_months_san['december'].append(int(station['value']))

# Sum for every month
for key in years_sum_months_san: 
    years_sum_months_san[key] = sum(years_sum_months_san[key])

# Convert dictionary to json file
with open('json_summonths_san_diego', 'w') as json_file_summonths_san_diego:
    json.dump(years_sum_months_san, json_file_summonths_san_diego)

# calculate sum for whole year
sumyear_san = sum(years_sum_months_san.values())

# calculate relative precipitation per month
perc_year_san = list()
for month in years_sum_months_san.values():
    perc_year_san.append((int(month)/sumyear_san)*100)
print(perc_year_san)

# All rain
allrain = list()
for station in station_data:
    allrain.append(int(station['value']))

totalrain = sum(allrain)
print(totalrain)


rain_city = {'Seattle': [(sumyear_seattle/totalrain)*100], 'Cincinatti': [(sumyear_cincinatti/totalrain)*100], 'Maui': [(sumyear_maui/totalrain)*100], 'San Diego': [(sumyear_san/totalrain)*100]}

print(rain_city)