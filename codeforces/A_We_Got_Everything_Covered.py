def solve():
    pass


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        alp = 'abcdefghijklmnopqrstuvwxyz'
        ans = alp[:k] * n
        print(ans)


if __name__ == "__main__":
    main()
