""" https://www.techiedelight.com/find-maximum-length-sub-array-having-given-sum/
nums[] = { 5, 6, -5, 5, 3, 5, 3, -2, 0 }
target = 8
 
Subarrays with sum 8 are
 
{ -5, 5, 3, 5 }
{ 3, 5 }
{ 5, 3 }
 
The longest subarray is { -5, 5, 3, 5 } having length 4 
 """


def main():
    arr = [5, 6, -5, 5, 3, 5, 3, -2, 0]
    S = 8

    target = 0
    d = {0: -1}
    maxlen = 0

    for i, num in enumerate(arr):
        target += num

        if target not in d:
            d[target] = i

        if target - S in d and maxlen < i - d[target - S]:
            maxlen = i - d[target - S]

    print(maxlen)


if __name__ == "__main__":
    main()
