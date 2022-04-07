def solve(A):
    odd = 0
    even = 0
    for num in A:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    all_even = float('inf')
    all_odd = float('inf')

    if odd % 2 == 0:
        all_even = odd // 2

    all_odd = even

    return min(all_even, all_odd)


def main():
    T = int(input())

    for tc in range(T):
        N = int(input())
        A = map(int, input().split())

        ans = solve(A)
        print(ans)


if __name__ == "__main__":
    main()
