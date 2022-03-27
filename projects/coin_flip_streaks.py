'''
Write a program to find out how often a streak of six heads or a streak of six tails comes up in a randomly generated list of heads and tails. Your program breaks up the experiment into two parts: the first part generates a list of randomly selected 'heads' and 'tails' values, and the second part checks if there is a streak in it. Put all of this code in a loop that repeats the experiment 10,000 times so we can find out what percentage of the coin flips contains a streak of six heads or tails in a row. As a hint, the function call random.randint(0, 1) will return a 0 value 50% of the time and a 1 value the other 50% of the time.
'''
import random
import statistics


def main():
    streaks = 0
    result = ['H', 'T']

    for i in range(10000):
        # Code that creates a list of 100 'heads' or 'tails' values.
        values = [result[random.randint(0, 1)] for i in range(100)]

        # Code that checks if there is a streak of 6 heads or tails in a row.
        accum_h = 0
        accum_t = 0
        for val in values:
            if val == 'H':
                accum_t = 0
                accum_h += 1
            else:
                accum_h = 0
                accum_t += 1

            if accum_h == 6 or accum_t == 6:
                streaks += 1
                break

    chance = str(round(streaks/10000 * 100, 2)) + '%'
    print('out of 10k simulations, there was %s case of six streak' % streaks)
    print('that\'s %s chance of six streaks occuring!' % chance)


# main()


# -------------------------------------------------------------------------------------------------



def other():
    '''what's the chance of someone scoring 6 streaks on their first try?'''
    streak0 = [0 for i in range(6)]
    streak1 = [1 for i in range(6)]
    streaks = 0

    for i in range(10000):
        values = [random.randint(0, 1) for i in range(6)]
        if values == streak0 or values == streak1:
            streaks += 1

    rounded = round(streaks/10000 * 100 ,2)
    chance = str(rounded) + '%'
    print('out of 10k simulations, this guy scored 6 streaks %s times' % streaks)
    print('that\'s %s chance' % chance)
    # result: about 3.17%
    # return rounded


# results = [other() for i in range(10)]

# final_ans = statistics.mean(results)

# print(final_ans)