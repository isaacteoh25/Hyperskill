import itertools

teams = ['Best-ever', 'Not-so-good', 'Amateurs', 'good']

my_iter = itertools.combinations(teams, 2)

try:
    for i in range(1000):
        print(next(my_iter))
    for team in itertools.combinations(teams, 2):
        print(team)
    print(*itertools.combinations(teams, 2), sep='\n')
except:
    pass