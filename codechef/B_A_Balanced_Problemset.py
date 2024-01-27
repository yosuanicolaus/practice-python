def solve():
    pass


def main():
    t = int(input())
    for _ in range(t):
        x, n = map(int, input().split())

        test_gcd = x // n

        while test_gcd > 1:
            remain = x - test_gcd * (n - 1)

            if remain < 0:
                test_gcd -= 1
            elif remain == 0 or remain % test_gcd == 0:
                break
            else:
                test_gcd -= 1

        print(test_gcd)


if __name__ == "__main__":
    main()


# first attempt below

# def main():
#     t = int(input())
#     for _ in range(t):
#         x, n = map(int, input().split())
#         max_gcd = 1

#         while True:
#             test_gcd = max_gcd + 1
#             remain = x - test_gcd * (n - 1)
#             if remain < 0:
#                 break
#             elif remain == 0 or remain % test_gcd == 0:
#                 max_gcd += 1
#             else:
#                 break
