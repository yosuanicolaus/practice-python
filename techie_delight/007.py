""" 
https://www.techiedelight.com/find-maximum-product-two-integers-array/
consider array {-10, -3, 5, 6, -2}. The maximum product is the (-10, -3) or (5, 6) pair.
"""


def main():
    arr = [-4, -3, 5, 4, -6]

    h1 = float('-inf')
    h2 = float('-inf')
    l1 = float('inf')
    l2 = float('inf')

    for num in arr:
        if num > h1:
            h2 = h1
            h1 = num
        elif num > h2:
            h2 = num

        if num < l1:
            l2 = l1
            l1 = num
        elif num < l2:
            l2 = num

    highest = max(l1*l2, h1*h2)
    print(highest)


if __name__ == "__main__":
    main()
