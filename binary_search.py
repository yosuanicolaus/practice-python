def binary_search(arr, target):
    low_idx = 0
    hi_idx = len(arr) - 1
    mid_idx = 0

    case = 0

    # exception for first and last
    if arr[low_idx] == target:
        return low_idx
    elif arr[hi_idx] == target:
        return hi_idx

    while low_idx < hi_idx:
        mid_idx = (low_idx + hi_idx) // 2
        case += 1
        print(
            f'Case #{case}: hi-{hi_idx}, low-{low_idx}, mid-{mid_idx}', end=', ')
        if hi_idx - low_idx == 1:
            print('NOT FOUND')
            break
        if arr[mid_idx] < target:
            # ignore left half
            low_idx = mid_idx
            print('going right')
        elif arr[mid_idx] > target:
            # ignore right half
            hi_idx = mid_idx
            print('going left')
        else:
            return mid_idx

    return 'NON EXISTENT'


def main():
    T = int(input('Enter number of test: '))

    # arr is [0, 10, 20, 30, ..., 970, 980, 990]
    arr = [i * 10 for i in range(100)]

    for tc in range(T):
        target = int(input("Enter Target: "))
        target_idx = binary_search(arr, target)

        print('target:', target)
        print('target index is', target_idx)


main()
