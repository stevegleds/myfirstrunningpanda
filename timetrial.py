import pandas as pd
import numpy as np
from readwrite import process_sourcefile

response = input('Use Brief csv (B) or Full (F) csv file? or complete Excel file (X)')
if response.lower() == 'b':
    sourcefile = 'timetrialbrief.csv'
elif response.lower() == 'f':
    sourcefile = 'timetrialfull.csv'
elif response.lower() == 'x':
    sourcefile = 'errraces.xlsm'
else:
    print("You didn't specify a correct file. I am going to use the quickest - Brief")
    sourcefile = 'timetrialbrief.csv'
print("We are using file: ", sourcefile)

try:
    print(process_sourcefile(sourcefile))
    # df = pd.read_csv(sourcefile)  # creates df with header conveniently inferred by default
    print("Reading file ... please wait")
except:
    print("The file is either out of date or not found. Please save an up to date file to this folder")

if response.lower() == 'x':
    df = pd.read_excel(sourcefile, sheetname='Timetrialresults', names=['Date', 'Runner', 'Time', 'Pace', 'Digitime'])
else:
    df = pd.read_csv(sourcefile)  # creates df with header conveniently inferred by default

def add_runner(runner, runner_list):
    return runner_list.append(runner)

def print_data(df):
    for index, row in df.iterrows():
        print(index, row['Runner'], row['Pace'])

runner_list = []
for index, row in df.iterrows():
    print(index, row['Runner'], row['Pace'])
    if row['Runner'] in runner_list:
        pass
    else:
        add_runner(row['Runner'], runner_list)


print('List of runners: ', runner_list)

byrunner = df.groupby('Runner')
byrunner['Digitime'].min()
byrunner['Digitime'].agg([np.min, np.sum, np.mean, len])
pb = byrunner['Digitime'].transform(min) == df['Digitime']
print(df[pb].sort(['Runner'], ascending=[True]))




