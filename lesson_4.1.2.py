def sal():
    try:
        time = float(input('Отработанное время в часах '))
        premium = int(input('Оклад в руб '))
        bonus = int(input('Премия в руб '))
        res = time * premium + bonus
        print(f'заработная плата работника  {res}')
    except ValueError:
        return print('Not a number')
sal()