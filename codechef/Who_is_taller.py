def solve():
    pass


def main():
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        if a < b:
            print("B")
        else:
            print("A")


if __name__ == "__main__":
    main()
