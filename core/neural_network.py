'''This module provides machine learning'''
#from pandas import read_csv, DataFrame, Series
from handlers.csv_handler import write_csv

data = 'nums,times'
write_csv(data, 'timetable.csv')

def build_model():
    pass