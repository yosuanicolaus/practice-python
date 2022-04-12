"""  https://www.techiedelight.com/sort-array-containing-0s-1s-2s-dutch-national-flag-problem/
Input:  { 0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0 }
 
Output: { 0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2 } 
"""


def main():
    arr = [0, 1, 2, 2, 1, 0, 0, 2, 0, 1, 1, 0]

    start = mid = 0
    pivot = 1
    end = len(arr) - 1

    while mid <= end:
        if arr[mid] < pivot:
            arr[mid], arr[start] = arr[start], arr[mid]
            start += 1
            mid += 1
        elif arr[mid] > pivot:
            arr[mid], arr[end] = arr[end], arr[mid]
            end -= 1
        else:
            mid += 1

    print(arr)


if __name__ == "__main__":
    main()
