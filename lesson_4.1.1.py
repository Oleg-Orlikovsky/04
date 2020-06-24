from sys import argv

name, time, premium, bonus = argv
try:
    time = int(time)
    premium = int(premium)
    bonus = int(bonus)
    res = time * premium + bonus
    print(f'заработная плата работника  {res}')
except ValueError:
    print('Not a number')