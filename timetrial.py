import pandas as pd
import numpy as np
import os
from readwrite import process_sourcefile, getfilelist

''' Ask user which file to use 
Then test to see if it is ok and create appropriate pandas datafile
'''
folder = os.path.join('','results')


'''
Building class to store info.
Instances are created from a dictionary created from the df
Need to use this to store PB and previous PB
'''
class Person:
    def __init__(self, name, created='today'):
        self.name = name.title()  # makes sure we use capital first letters
        self.created = created

    def __str__(self):
        return '{} started on {}'.format(self.name, self.created)


# # TODO see if this is used anywhere
# def print_data(df):
#     for index, row in df.iterrows():
#         print('These are the runners and their paces for all races:')
#         print(index, row['Runner'], row['Pace'])


'''
This section is work in progress to identify pbs
'''
# jan2015 = df[df.Date == '2015-01-05']
# feb2015 = df[df.Date == '2015-02-02']
# print('The results for January 2015 were: \n', jan2015)
# print('The results for February 2015 were: \n', feb2015)
# print('The average pace for January was: ', jan2015['Digitime'].mean(), '\n and for February was: ', feb2015['Digitime'].mean())
# # print(df[df['Runner'].str.contains('Craig Bingham')])  # prints all Craig's results
# latest_results = feb2015
# previous_results = jan2015
# for runner in runnerdict:
#     if runner in latest_results.Runner.values and runner in previous_results.Runner.values:
#         latest_race = latest_results[latest_results['Runner'].str.contains(runner)]
#         previous_race = previous_results[previous_results['Runner'].str.contains(runner)]
#         # print(latest_race)
#         # print(previous_race)
#         print('Latest time for {} was {} minutes'.format(runner, latest_race['Digitime'].values))
#         print('Previous time for {} was {} minutes' .format(runner, previous_race['Digitime'].values))
#         print('{} has improved by {} seconds \n' .format(runner, 60*(previous_race['Digitime'].values - latest_race['Digitime'].values)))

if __name__ == "__main__":
    print('Welcome to the timetrial results')


# Present list of files to the console
filelist = getfilelist(folder)
for file in enumerate(filelist):
    print(file)
# Ask user to choose their file
sourcefile = os.path.join(folder, filelist[int(input('Which file do you want to use? '))])
print("We are using file: ", sourcefile)

try:
    print(process_sourcefile(sourcefile))
    # df = pd.read_csv(sourcefile)  # creates df with header conveniently inferred by default
    print("Reading file ... please wait")
except:
    print("The file is either out of date or not found. Please save an up to date file to this folder")

df = pd.read_csv(sourcefile, parse_dates=['Date'],
                 dayfirst=True)  # creates df with header conveniently inferred by default

df = df.sort_values(by=['Date', 'Runner'], ascending=[True, True])
'''
runnerdict will store information that will be used to create person instances
'''
runnerdict = {}
print('pandas file is:', df)
for index, row in df.iterrows():
    if runnerdict.get(row['Runner']):
        print('runner exists')
        pass
    else:
        runnerdict[row['Runner']] = row['Date']
print(len(runnerdict))
# print(runnerdict)
print(runnerdict)
runners = {}  # Empty dict to store runner objects
for k, v in runnerdict.items():
    runners[k] = Person(k, v)
print('runner people created')
for runner in runners:
    print(runners[runner])

# TODO document what these pandas tools are doing
byrunner = df.groupby('Runner')
byrunner['Digitime'].min()
byrunner['Digitime'].agg([np.min, np.sum, np.mean, len])
pb = byrunner['Digitime'].transform(min) == df['Digitime']