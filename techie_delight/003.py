""" https://www.techiedelight.com/find-sub-array-with-0-sum/ """


def zero_sum_sub(arr):
    d = {}
    total = 0
    d[0] = [-1]
    res = []

    for i, num in enumerate(arr):
        total += num
        if total in d:
            l = d.get(total)
            for val in l:
                print('sublist is', val+1, i)
        d.setdefault(total, []).append(i)

    return res


def main():
    arr = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]
    zero_sum_sub(arr)


if __name__ == "__main__":
    main()
