'''https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb33e/00000000009e7021'''


def solve(target: str, produced: str):
    a, b = 0, 0
    dc = 0

    while a < len(target):
        if b == len(produced):
            return 'IMPOSSIBLE'
        if target[a] != produced[b]:
            dc += 1
            b += 1
        else:
            a += 1
            b += 1

    dc += len(produced) - b
    return dc


def main():
    T = int(input())

    for tc in range(1, T+1):
        target = input()
        produced = input()

        ans = solve(target, produced)
        print(f'Case #{tc}: {ans}')


if __name__ == "__main__":
    main()
