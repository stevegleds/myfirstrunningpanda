import pandas as pd
from readwrite import process_sourcefile

response = input('Use Brief csv (B) or Full (F) csv file? or complete Excel file (X)')
if response.lower() == 'f':
    sourcefile = 'timetrialbrief.csv'
elif response.lower() == 'f':
    sourcefile = 'timetrialfull.csv'
else:
    sourcefile = 'errraces.xlsm'
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

runner_list = []
for index, row in df.iterrows():
    print(index, row['Runner'], row['Pace'])
    if row['Runner'] in runner_list:
        pass
    else:
        add_runner(row['Runner'], runner_list)

print('List of runners: ', runner_list)

pbs = df.groupby(['Runner'])['Pace'].transform(min) == df['Pace']
print(df[pbs].sort_index('Runner'))




