import string


def solve():
    pass


def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        alp = string.ascii_lowercase
        ans = alp[:k] * n
        print(ans)


if __name__ == "__main__":
    main()
