""" https://www.techiedelight.com/sort-binary-array-linear-time/
Input:  { 1, 0, 1, 0, 1, 0, 0, 1 }
Output: { 0, 0, 0, 0, 1, 1, 1, 1 } 
 """


def main():
    arr = [1, 0, 1, 0, 1, 0, 0, 1]

    a, b = 0, len(arr) - 1
    while a < b:
        if arr[a] == 0:
            a += 1
            continue
        elif arr[b] == 1:
            b -= 1
            continue

        arr[a], arr[b] = arr[b], arr[a]

    print(arr)


if __name__ == "__main__":
    main()
