def binary_search(arr, low, high, target):
    if high < low:
        return -1

    mid = (low + high) // 2

    if arr[mid] < target:
        return binary_search(arr, mid+1, high, target)
    elif arr[mid] > target:
        return binary_search(arr, low, mid-1, target)
    else:
        return mid


def main():
    while True:
        arr = list(range(1, 100, 2))  # [1,3,5,7,...,99]
        target = int(input())

        try:
            ans = binary_search(arr, 0, len(arr), target)
            actual = arr.index(target)
        except:
            ans = -1
            actual = 'not found'
        print(ans, actual)


if __name__ == "__main__":
    main()
