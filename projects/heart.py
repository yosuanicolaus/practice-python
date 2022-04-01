def space(i: int):
    return i * ' '


def solution(n: int):
    ans = ''

    # top section
    for i in range(n + 1):
        outer = n - i
        inside = n + (i - 1) * 2  # except firstline
        middle = n * 2 - i * 2 - 1

        newline = space(outer) + 'x' + space(inside) + 'x' + \
            space(middle) + 'x' + space(inside) + 'x' + space(outer) + '\n'

        if i == 0:
            newline = space(outer) + n * 'x' + \
                space(middle) + n * 'x' + space(outer) + '\n'
        elif i == n:
            newline = 'x' + space(inside) + 'x' + space(inside) + 'x\n'

        ans += newline
    # mid section
    heart_width = 2 * (n + 2 * (n - 1)) + 1
    for i in range(n):
        ans += 'x' + space(heart_width) + 'x\n'
    # bottom section
    for i in range(3 * n):
        if i == 0:
            continue
        middle = heart_width - i * 2
        last_heart = 'x'

        if i == 3*n - 1:
            last_heart = ''

        ans += space(i) + 'x' + space(middle) + last_heart + '\n'

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
