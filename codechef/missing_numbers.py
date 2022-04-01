'''
https://www.codechef.com/problems/MISS_NUM

Sample Input 1
2
-1 72 0 17
1 4 5 6

Sample Output 1
8 9
-1 -1
'''


def solve(A, S, M, D):
    a = (A + S) // 2
    b = abs(A - S) // 2

    if a <= 0 or b <= 0 or a > 1e4 or b > 1e4:
        return [-1, -1]

    if (a * b == M and a // b == D) or (a * b == D and a // b == M):
        return [a, b]

    return [-1, -1]


def main():
    T = int(input())
    for tc in range(T):
        A, S, M, D = map(int, input().split())
        combs = [
            [A, S, M, D],
            [A, M, S, D],
            [A, D, S, M],
            [S, M, A, D],
            [S, D, A, M],
            [M, D, A, S],
        ]
        for comb in combs:
            a, b = solve(*comb)
            if (a, b) != (-1, -1):
                break
        print(a, b)


if __name__ == "__main__":
    main()
