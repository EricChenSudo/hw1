#!/usr/bin/env python3 

# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '107061237.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)
#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
# target_data = data[:10]

# first, preprocessing the data. 
# In TEMP column, change '-99.000' or '-999.00' with 'None'
for i in range(len(data)):
    if data[i]['TEMP'] == '-99.000' or data[i]['TEMP'] == '-999.000':
        data[i]['TEMP'] = 'None'

# target_data will be used to store the answer, so we need to get the space first.
# And because the answer need to be arranged in the lexicographical order, I declare them first.
target_data = [['C0A880'], ['C0F9A0'], ['C0G640'], ['C0R190'], ['C0X260']]
# after arranged the order, I made up the remaining space needed in the back of each elements.
# And I assume maximum TEMP of each stations are 'None' first.
for i in range(5):
    target_data[i].append('None')

# Start to find the result in each station.
# The methods I used are
# 1. Use for loop to let me can scan through all the station.
# 2. check whether  the temperature of station[i] is 'None' or not.
#    If the temperature of the station[i] is 'None', we can skip directly to check the next station,
#    Because we assume the temperature of the station is 'None' already.
# 3. If the temperature of the station[i] isn't 'None', we need to check which one is bigger, 
#    the temperature stored in the target_data or the temperature of the station[i].
#    Finally, store the bigger one into the target_data.(Remember, station_ID should be the same)
# (NOTE)Because the datatype of the temperature stored in the data list is string, we need to convert it to float.
# (NOTE)If the temperature stored in the target_data is 'None' and the temperature of the station[i] isn't 'None', 
#       we can assign the temperature of the station[i] to the target data directly.
for i in range(len(data)):
    if data[i]['TEMP'] != 'None':
        if data[i]['station_id'] == target_data[0][0]:   # processing the temperature of 'C0A880' station
            if target_data[0][1] == 'None':
                target_data[0][1] = float(data[i]['TEMP'])
            elif float(data[i]['TEMP']) > target_data[0][1]:
                target_data[0][1] = float(data[i]['TEMP'])
        elif data[i]['station_id'] == target_data[1][0]: # processing the temperature of 'C0F9A0' station
            if target_data[1][1] == 'None':
                target_data[1][1] = float(data[i]['TEMP'])
            elif float(data[i]['TEMP']) > target_data[1][1]:
                target_data[1][1] = float(data[i]['TEMP'])
        elif data[i]['station_id'] == target_data[2][0]: # processing the temperature of 'C0G640' station
            if target_data[2][1] == 'None':
                target_data[2][1] = float(data[i]['TEMP'])
            elif float(data[i]['TEMP']) > target_data[2][1]:
                target_data[2][1] = float(data[i]['TEMP'])
        elif data[i]['station_id'] == target_data[3][0]: # processing the temperature of 'C0R190' station
            if target_data[3][1] == 'None':
                target_data[3][1] = float(data[i]['TEMP'])
            elif float(data[i]['TEMP']) > target_data[3][1]:
                target_data[3][1] = float(data[i]['TEMP'])
        elif data[i]['station_id'] == target_data[4][0]: # processing the temperature of 'C0X260' station
            if target_data[4][1] == 'None':
                target_data[4][1] = float(data[i]['TEMP'])
            elif float(data[i]['TEMP']) > target_data[4][1]:
                target_data[4][1] = float(data[i]['TEMP'])
#=======================================

# Part. 4
#=======================================
# Print result
print(target_data)
#========================================

