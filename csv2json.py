#!/usr/bin/env python3

import csv
import json
import os
import glob


def csv_to_json(csvFilePath, jsonFilePath, delimiter):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf, delimiter=delimiter)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


print('***************************')
print('*** Convert CSV to JSON ***')
print('***************************')
print('')

# Get current directory path
dir_path = input('Directory path or RETURN for current directory:\n')
if not dir_path:
    dir_path = os.path.dirname(os.path.realpath(__file__))

# Check if path exists
if not os.path.exists(dir_path):
    quit('Invalid path! Sorry, try again.')

print('\nSelected directory: ')
print('*******************')
print(dir_path)

# Show available files
print('\nChoose csv file: ')
print('****************')
csv_files = glob.glob(dir_path + "/*.csv")
index = 1
for csv_file in csv_files:
    print('[' + str(index) + ']: ' + csv_file)
    index += 1

# Enter filename
fileIndex = input('\nChoose file [Enter number]:')

# Choose file
if not fileIndex or int(fileIndex) > len(csv_files):
    quit('Invalid selection. Sorry, try again.')

# Absolute file path
filepath = csv_files[int(fileIndex) -1]

# Remove file extension
filepath = filepath[:-4]

# Final file path
csvFilePath = r''+filepath+'.csv'
jsonFilePath = r''+filepath+'.json'

# Choose delimiter
delimiter = input('\nChoose delimiter (Default ;):')
if not delimiter:
    delimiter = ';'

# Create JSON file
csv_to_json(csvFilePath, jsonFilePath, delimiter)

print('\nGenerate JSON file: ')
print('*******************')
print('Filename Input:', csvFilePath)
print('Filename Output:', jsonFilePath)


#@Todo: Custom delimiter input / Delimiter detection