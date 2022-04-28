def solve(p, w, c):
    dp = [[-1 for _ in range(len(p))] for _ in range(c + 1)]
    return ksr(dp, p, w, c, 0)


def ksr(dp, p, w, c, i):
    if c <= 0 or i == len(p):
        return 0
    if dp[c][i] != -1:
        return dp[c][i]

    p1 = 0
    if w[i] <= c:
        p1 += p[i] + ksr(dp, p, w, c-w[i], i+1)

    p2 = ksr(dp, p, w, c, i+1)

    dp[c][i] = max(p1, p2)
    return dp[c][i]


def main():
    print(solve([1, 6, 10, 16], [1, 2, 3, 5], 5))
    print(solve([1, 6, 10, 16], [1, 2, 3, 5], 6))
    print(solve([1, 6, 10, 16], [1, 2, 3, 5], 7))


if __name__ == "__main__":
    main()
