import math


def prime_upto(n):
    arr = list(range(2, n+1))

    for i, num in enumerate(arr):
        if num == 0:
            continue

        i += num
        while i < len(arr):
            arr[i] = 0
            i += num

    arr = list(filter(lambda x: x != 0, arr))
    return arr


def solve(nums):
    upto = math.ceil(math.sqrt(nums[-1]))
    siever = prime_upto(upto)
    arr = nums.copy()
    first = arr[0]

    for prime in siever:
        if first % prime == 0:
            i = 0
        else:
            i = prime - (first % prime)

        if i < len(arr) and arr[i] == prime:
            i += prime

        while i < len(arr):
            arr[i] = 0
            i += prime

    arr = list(filter(lambda x: x > 1, arr))
    return arr


def main():
    T = int(input())

    for tc in range(T):
        n, m = map(int, input().split())
        nums = list(range(n, m+1))

        ans = solve(nums)

        for num in ans:
            print(num)

        if tc != T-1:
            print()


if __name__ == "__main__":
    main()
