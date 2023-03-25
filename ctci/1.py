import string


def is_unique(str: str):
    seen = set()
    for ch in str:
        if ch in seen:
            return False
        seen.add(ch)
    return True


def check_permutation(s1: str, s2: str):
    # s1 is permutation of s2 or vice versa
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    c1 = {}
    c2 = {}

    for ch in string.ascii_lowercase:
        c1[ch] = 0
        c2[ch] = 0
    for ch in s1:
        c1[ch] += 1
    for i in range(len(s2)):
        c2[s2[i]] += 1
        if i >= len(s1) - 1:
            if c1 == c2:
                return True
            c2[s2[i - len(s1) + 1]] -= 1

    return False


def urlify(str: str, n: int):
    '''
    Input: "Mr John Smith    ", 13
    Output:"Mr%20John%20Smith"
    '''
    res = list(str)
    a = b = len(str) - 1
    while str[a] == ' ':
        a -= 1

    while a != b and b >= 0:
        cha = str[a]
        if cha == ' ':
            res[b], res[b-1], res[b-2] = '0', '2', '%'
            b -= 3
        else:
            res[b] = res[a]
            b -= 1
        a -= 1

    return ''.join(res)


def palindrome_permutation(s: str):
    # if more than 1 of the ch count is odd, palindrome is not possible
    odd_count = 0
    count = {}

    for ch in s:
        if ch not in string.ascii_letters:
            continue
        ch = ch.lower()
        count[ch] = 1 + count.get(ch, 0)

    for ch, cc in count.items():
        if cc % 2 == 1:
            odd_count += 1
            if odd_count == 2:
                return False

    return True


def one_edit_away(s1: str, s2: str):
    if len(s1) == len(s2):
        return one_replace_away(s1, s2)
    if len(s1) - len(s2) == 1:
        return one_insert_away(s2, s1)
    if len(s2) - len(s1) == 1:
        return one_insert_away(s1, s2)
    return False


def one_replace_away(s1: str, s2: str):
    replace_count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            replace_count += 1
            if replace_count == 2:
                return False
    return True


def one_insert_away(s1: str, s2: str):
    # len(s2) - len(s1) == 1, s1 smaller by 1
    insert_count = 0
    a, b = 0, 0
    while a < len(s1) and b < len(s2):
        if s1[a] != s2[b]:
            insert_count += 1
            b += 1
            if insert_count == 2:
                return False
        a += 1
        b += 1
    return True


def rotate_matrix(matrix: list[list[int]]):
    n = len(matrix)
    for base in range(n // 2):
        for i in range(n - 2 * base - 1):
            ar, ac = base, base + i
            br, bc = base + i, n - 1 - base
            cr, cc = n - 1 - base, n - 1 - base - i
            dr, dc = n - 1 - base - i, base
            matrix[ar][ac], matrix[br][bc], matrix[cr][cc], matrix[dr][dc] = \
                matrix[dr][dc], matrix[ar][ac], matrix[br][bc], matrix[cr][cc]


def zero_matrix(matrix: list[list[int]]):
    zero_rows = []
    zero_cols = []
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if matrix[r][c] == 0:
                zero_rows.append(r)
                zero_cols.append(c)

    for r in zero_rows:
        for c in range(len(matrix[0])):
            matrix[r][c] = 0

    for c in zero_cols:
        for r in range(len(matrix)):
            matrix[r][c] = 0


def is_rotation(s1: str, s2: str):
    if len(s1) != len(s2):
        return False

    for i in range(len(s2)):
        ns = s2[i:] + s2[:i]
        if ns == s1:
            return True

    return False


# print(urlify("Mr John Smith    ", 13))
# print(palindrome_permutation("Taco Cat"))
# print(one_edit_away('pale', 'ple'))  # -> true
# print(one_edit_away('pales', 'pale'))  # -> true
# print(one_edit_away('pale', 'bale'))  # -> true
# print(one_edit_away('pale', 'bake'))  # -> false
# m = []
# c = 1
# for _ in range(6):
#     m.append([])
#     for _ in range(6):
#         m[-1].append(c)
#         c += 1
# for l in m:
#     print(l)
# m = [
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 0, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 1, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1],
# ]
# zero_matrix(m)
# for list in m:
#     print(list)
# print(is_rotation("waterbottle", "erbottlewat"))
