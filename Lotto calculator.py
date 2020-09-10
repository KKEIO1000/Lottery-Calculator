"""Lottery Calculator"""

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom

def balls():
    """Asks the user about the standard balls"""
    while True:
        try:
            balls = int(input('Enter the number of available balls: '))
            break
        except:
            print('invalid input')

    while True:
        try:
            choices = int(input('Enter the amount of balls to select: '))
            break
        except:
            print('invalid input')
    while True:
        try:
            cost = float(input('Enter the cost of one ticket: '))
            break
        except:
            print('invalid input')
    return balls, choices, cost


def ask_for_bonus():
    while True:
        bonus = input('Are there bonus balls? y/n: ')

        if bonus == 'n':
            return False
        elif bonus =='y':
            return True
        else:
            print('invalid input')

def bonus_balls():
    """Asks the user about the bonus balls"""
    while True:
        try:
            b_balls = int(input('Enter the number of available bonus balls: '))
            break
        except:
            print('invalid input')

    while True:
        try:
            b_choices = int(input('Enter the amount of bonus balls to select: '))
            break
        except:
            print('invalid input')

    return b_balls, b_choices

def calculate_balls(balls, choices, cost):
    tot = ncr(balls, choices)
    print('Lucky you')
    print('*' * 100)
    for i in range(2, choices+1):
        print(f'Your likelihood of matching {i} balls is 1 in {int(tot/(ncr(choices, i) * ncr(balls - choices, choices - i)))}')
    print('*' * 100)
    print(f'You are expected to spend {int(cost*tot)} in order to win the jackpot, good luck!')

def calculate_balls_with_bonus(balls, choices, b_balls, b_choices, cost):
    print('Lucky you')
    print('*' * 100)
    tot = ncr(balls, choices)
    tot_b = ncr(b_balls, b_choices)
    for i in range(2, choices+1):
        for j in range(0, b_choices+1):
            main = tot /(ncr(choices, i) * ncr(balls - choices, choices - i))
            bonus = tot_b/(ncr(b_choices, j) * ncr(b_balls - b_choices, b_choices - j))
            print(f'Your likelihood of matching {i} balls and {j} bonus balls is 1 in {int(main*bonus)}')
    print('*' * 100)
    print(f'You are expected to spend {int(cost*tot*tot_b)} in order to win the jackpot, good luck!')

balls, choices, cost = balls()
if ask_for_bonus():
    b_balls, b_choices = bonus_balls()
    calculate_balls_with_bonus(balls, choices, b_balls, b_choices, cost)
else: calculate_balls(balls, choices, cost)