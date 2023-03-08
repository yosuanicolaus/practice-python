def recursive(count: int, open_count: int, close_count: int):
    if count == 0 and open_count == 0 and close_count == 0:
        return 1
    if count < 0 or open_count < 0 or close_count < 0:
        return 0

    return recursive(count + 1, open_count - 1, close_count) + recursive(count-1, open_count, close_count - 1)


def BracketCombinations(num):
    return recursive(0, num, num)


print(BracketCombinations(1))
print(BracketCombinations(2))
print(BracketCombinations(3))
print(BracketCombinations(4))
