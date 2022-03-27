def solution(n: int):
    ans = ''
    lower = []
    for i in range(n + 1):
        first_space = n - i
        second_space = i * 2 - 1
        last_star = '*'

        if i == 0:
            last_star = ''

        newline = (first_space * ' ') + '*' + \
            (second_space * ' ') + last_star + '\n'
        ans += newline

        lower.append(newline)

    lower.pop()
    for i in range(n):
        ans += lower.pop()

    return ans


def main():
    T = int(input())
    for tc in range(T):
        n = int(input())

        ans = solution(n)
        print(f'Case #{tc+1}:')
        print(ans)


if __name__ == "__main__":
    main()
