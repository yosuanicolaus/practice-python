def change_safe(unsafe: str):
    chars = 'abcde'
    for ch in chars:
        if ch != unsafe:
            return ch


def solve(S: str, A: str):
    S = [ch for ch in S]
    A = [ch for ch in A]

    # if impossible
    a, b = 0, 0
    while a < len(S):
        if S[a] == A[b]:
            b += 1
        a += 1
        if b == len(A):
            return -1

    safe_char = 'a'
    unsafe_idx = 0
    if safe_char == A[unsafe_idx]:
        safe_char = change_safe(A[unsafe_idx])

    new_str = ''

    for ch in S:
        if ch == '?':
            new_str += safe_char
        elif ch == A[unsafe_idx] and unsafe_idx + 1 < len(A):
            unsafe_idx += 1
            safe_char = change_safe(A[unsafe_idx])
            new_str += ch
        else:
            new_str += ch

    return new_str


def main():
    T = int(input())

    for tc in range(T):
        n, m = map(int, input().split())
        S = input()
        A = input()

        ans = solve(S, A)
        print(ans)


if __name__ == "__main__":
    main()
