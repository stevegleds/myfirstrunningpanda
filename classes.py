import pandas as pd
import os
import numpy as np
from readwrite import process_sourcefile
folder = os.path.join('','results')
print('folder is:', folder)
sourcefile = os.path.join(folder, 'timetrial160905.csv')
print('source file is: ', sourcefile)
df = pd.read_csv(sourcefile, parse_dates=['Date'], dayfirst=True)  # creates df with header conveniently inferred by default

class Person:
    def __init__(self, name, created='today'):
        self.name = name.title()  # makes sure we use capital first letters
        self.created = created
        self.prevPace = None
        self.prevTime = None
        self.pbPace = None
        self.pbTime = None

    def __str__(self):
        return '{} started on {}'.format(self.name, self.created)

    def updatePrevPB(self, prevPace, prevTime):
        self.prevPace = prevPace
        self.prevTime = prevTime

    def updatePB(self, pbPace, pbTime):
        self.pbPace = pbPace, pbTime

runnerdict = dict(zip(df.Runner, df.Date))
runners = {}
for k, v in runnerdict.items():
    runners[k] = Person(k, v)
print('runner people created')

def updatePBs(runner, pace, time):
    runners[runner].updatePB(pace, time)

for runner in runners:
    updatePBs(runner, 9.50, "00:09:30")

for runner in runners:
    print(runners[runner].pbPace)