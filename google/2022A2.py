'''https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7997'''


def solve(N: str):
    total = 0
    for sdg in N:
        total += int(sdg)
    rem = (9 - total % 9) % 9

    idx = 0
    if rem == 0:
        idx += 1
    while idx < len(N):
        if rem < int(N[idx]):
            break
        idx += 1

    ans = N[:idx] + str(rem) + N[idx:]
    return ans


def main():
    T = int(input())

    for tc in range(1, T+1):
        N = input()

        ans = solve(N)
        print(f'Case #{tc}: {ans}')


if __name__ == "__main__":
    main()
