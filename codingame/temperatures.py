def main():
    n = int(input())  # the number of temperatures to analyse
    ans = 0
    closest = float('inf')

    for i in input().split():
        # t: a temperature expressed as an integer ranging from -273 to 5526
        t = int(i)
        if abs(t) < closest:
            closest = abs(t)
            ans = t
        elif abs(t) == closest and ans < t:
            ans = t

    print(ans)


if __name__ == "__main__":
    main()
