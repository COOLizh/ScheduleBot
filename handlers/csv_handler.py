'''This module provides all methods to work with csv files'''

def write_csv(data, path):
    '''Write data to a CSV file path'''
    with open(path, 'w') as csv_file:
        csv_file.write(data)
    csv_file.close()
