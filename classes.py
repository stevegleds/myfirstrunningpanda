class Person:
    def __init__(self, name, created='today'):
        self.name = name.title()  # makes sure we use capital first letters
        self.created = created

    def __str__(self):
        return '{} started on {}'.format(self.name, self.created)


def add_runner(runner, date, runner_list):
    return runner_list.append([runner, date])

runnerdict = dict(zip(df.Runner, date(df.Date)))
runners = {}
for k, v in runnerdict.items():
    runners[k] = Person(k, v)

for runner in runners:
    print(runners[runner])

