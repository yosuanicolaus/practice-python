def solve(A):
    total = 0
    for num in A:
        total += num

    count = 0
    i = 1
    while total >= i:
        total -= i
        i += 1
        count += 1

    return count


def main():
    T = int(input())

    for tc in range(T):
        N = int(input())
        A = list(map(int, input().split()))

        ans = solve(A)
        print(ans)


if __name__ == "__main__":
    main()
