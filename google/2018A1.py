'''https://codingcompetitions.withgoogle.com/kickstart/round/0000000000050edf/00000000000510ed'''


def solve(N: str):
    plus = 0
    minus = 0
    nums = ''
    for i, strdigit in enumerate(N):
        if int(strdigit) % 2 != 0:
            nums = N[i:]
            break
    else:
        return 0

    mingoal = int(str(int(nums[0]) - 1) + '8' * (len(nums) - 1))
    maxgoal = int(str(int(nums[0]) + 1) + '0' * (len(nums) - 1))

    if nums[0] == '9':
        plus = float('inf')
        minus = int(nums) - mingoal
    else:
        plus = maxgoal - int(nums)
        minus = int(nums) - mingoal

    return min(plus, minus)


def main():
    T = int(input())

    for tc in range(1, T+1):
        N = input()

        ans = solve(N)
        print(f'Case #{tc}: {ans}')


if __name__ == "__main__":
    main()
