'''
source : https://inventwithpython.com/bigbookpython/project2.html

The Birthday Paradox, also called the Birthday Problem, is the surprisingly high probability that two people will have the same birthday even in a small group of people. In a group of 70 people, there's a 99.9 percent chance of two people having a matching birthday. But even in a group as small as 23 people, there's a 50 percent chance of a matching birthday. This program performs several probability experiments to determine the percentages for groups of different sizes. We call these types of experiments, in which we conduct multiple random trials to understand the likely outcomes, Monte Carlo experiments.
'''
"""
Birthday Paradox, by Al Sweigart al@inventwithpython.com
--snip--
How many birthdays shall I generate? (Max 100)
> 23
Here are 23 birthdays:
Oct 9, Sep 1, May 28, Jul 29, Feb 17, Jan 8, Aug 18, Feb 19, Dec 1, Jan 22,
May 16, Sep 25, Oct 6, May 6, May 26, Oct 11, Dec 19, Jun 28, Jul 29, Dec 6,
Nov 26, Aug 18, Mar 18
In this simulation, multiple people have a birthday on Jul 29
Generating 23 random birthdays 100,000 times...
Press Enter to begin...
Let's run another 100,000 simulations.
0 simulations run...
10000 simulations run...
--snip--
90000 simulations run...
100000 simulations run.
Out of 100,000 simulations of 23 people, there was a
matching birthday in that group 50955 times. This means
that 23 people have a 50.95 % chance of
having a matching birthday in their group.
That's probably more than you would think!
"""

import random
def main():
    print('How many people in the room?')
    num = int(input())

    birthdays = [random.randint(1, 365) for i in range(num)]

    print('here are %s birthdays' % num)
    print(birthdays)

    same_days = get_same_birthdays(birthdays)
    if same_days == []:
        print('there was no same birthday on this room')
    else:
        print('on this room, there was %s occurence of same birthdays' %
              len(same_days))
        print('those days are', sorted(same_days))

    print('Now, let\'s run this simulation 100,000 times')
    print('Generating %s random birthday 100,000 times...' % num)

    true_count = 0
    for i in range(100_000):
        if i % 10_000 == 0:
            print(str(i), 'simulations run...')
        birthdays = [random.randint(1, 365) for i in range(num)]
        if has_same_birthday(birthdays):
            true_count += 1

    chance = str(round((true_count / 100_000) * 100, 2)) + '%'
    print()
    print('simulation completed!')
    print(f'out of 100,000 simulations of {num} people,')
    print(f'there was {true_count} matching birthday in that group')
    print(f'this means there was {chance} chance of {num} people')
    print('having a matching birthday in the room')
    print('that\'s probaly more than you think!')


def get_same_birthdays(birthdays: list) -> list:
    '''use hash tables (dictionary)'''
    days = {}
    for birthday in birthdays:
        if birthday in days:
            days[birthday] += 1
        else:
            days[birthday] = 1

    same_days = [day for day in days if days[day] > 1]
    return same_days


def has_same_birthday(birthdays: list) -> bool:
    mapped = []
    for day in birthdays:
        if day in mapped:
            return True
        else:
            mapped.append(day)
    return False


main()
