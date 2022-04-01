'''First and last index of target'''
""" (arr is sorted)
arr = [2,4,5,5,5,5,5,7,9,9]
target = 5
output = [2,6]
explanation: target 5 starts at index 2
             and ends at index 6
"""


def find_first(arr: list, target: int):
    '''find first index of target
    it means before the target isn't target'''
    low = 0
    high = len(arr) - 1

    if arr[low] == target:
        return low
    elif arr[high] == target and arr[high - 1] != target:
        return high
    
    while low < high:
        mid = (low + high) // 2

        if arr[mid] == target and arr[mid - 1] != target:
            return mid
        elif arr[mid] < target:
            low = mid
        elif arr[mid] >= target:
            high = mid
    
    return -1


def find_last(arr: list, target: int):
    '''find last index of target
    it means after the target isn't target'''
    low = 0
    high = len(arr) - 1

    if arr[low] == target and low + 1 < len(arr) and arr[low + 1] != target:
        return low
    elif arr[high] == target:
        return high
    
    while low < high:
        mid = (low + high) // 2

        if arr[mid] == target and arr[mid + 1] != target:
            return mid
        elif arr[mid] <= target:
            low = mid
        elif arr[mid] > target:
            high = mid
    
    return -1


def solve(arr: list, target: int) -> list:
    start = find_first(arr, target)
    end = find_last(arr, target)

    return [start, end]


def main():
    T = int(input())

    for tc in range(T):
        arr = list(map(int, input().split(' ')))
        target = int(input())

        ans = solve(arr, target)
        print(f'Case #{tc+1}: {ans}')


# main()

arr = [1, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6]
target = 5

print(solve(arr, target))

