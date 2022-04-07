def create_contagious(arr):
    blocks = []
    a, b = 0, 1
    while b < len(arr):
        if arr[b] - arr[b - 1] == 1:
            b += 1
        else:
            blocks.append(arr[a:b])
            a = b
            b += 1
        if b == len(arr):
            blocks.append(arr[a:b])
    return blocks


def solve(A: list):
    A = list(set(A))
    A.sort()
    if A[0] >= 1:
        # MEX = 0
        return A[0] - 1
    elif A[0] == 0 and 1 not in A:
        # MEX = 1 -> infinite
        return -1

    # divide to group of contagious nums
    blocks = create_contagious(A)
    total_k = 0
    MEX = blocks[0][-1] + 1

    for i, nums in enumerate(blocks):
        if i == 0:
            continue

        if len(nums) >= MEX - 1:
            total_k += 1

    return total_k


def main():
    T = int(input())

    for tc in range(T):
        n = int(input())
        A = list(map(int, input().split()))

        ans = solve(A)
        print(ans)


if __name__ == "__main__":
    main()
