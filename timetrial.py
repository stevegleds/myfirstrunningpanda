import pandas as pd
from readwrite import process_sourcefile

try:
    print(process_sourcefile('timetrial.csv'))
    data = pd.read_csv('timetrial.csv')  # creates df with header conveniently inferred by default
    print(data)
except:
    print("The file is either out of date or not found. Please save an up to date file to this folder")

def add_runner(runner, runner_list):
    return runner_list.append(runner)

runner_list = []
for index, row in data.iterrows():
    print(index, row['Runner'], row['Pace'])
    if row['Runner'] in runner_list:
        pass
    else:
        add_runner(row['Runner'], runner_list)

print('List of runners: ', runner_list)

pbs = data.groupby(['Runner'])['Pace'].transform(min) == data['Pace']
print(data[pbs])




