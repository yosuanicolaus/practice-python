def solve(target: str, actual: str):
    ans = 0
    t_idx = 0
    a_idx = 0
    t_len = len(target)
    a_len = len(actual)

    while a_idx < a_len and t_idx < t_len:
        if actual[a_idx] == target[t_idx]:
            t_idx += 1
        else:
            ans += 1
        a_idx += 1

    if t_idx < t_len:
        return 'IMPOSSIBLE'
    if a_idx < a_len:
        ans += a_len - a_idx
    return ans


def main():
    test = int(input())
    for i in range(test):
        target = str(input())
        actual = str(input())

        ans = solve(target, actual)
        print(f"Case #{i+1}: {ans}")


if __name__ == "__main__":
    main()
