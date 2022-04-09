'''https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7021'''
""" AC - TLE """


def is_interesting(i):
    product = 1
    dsum = 0
    for sdg in str(i):
        product *= int(sdg)
        dsum += int(sdg)
    return product % dsum == 0


def solve(A, B):
    i = A
    interesting = 0
    while i <= B:
        if is_interesting(i):
            interesting += 1
        i += 1
    return interesting


def main():
    T = int(input())

    for tc in range(1, T+1):
        A, B = map(int, input().split())

        ans = solve(A, B)
        print(f'Case #{tc}: {ans}')


if __name__ == "__main__":
    main()
