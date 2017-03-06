import pandas as pd
from readwrite import process_sourcefile

try:
    print(process_sourcefile('timetrial.csv'))
    data = pd.read_csv('timetrial.csv')  # creates df with header conveniently inferred by default
    print(data)
except:
    print("The file is either out of date or not found. Please save an up to date file to this folder")

for dat

