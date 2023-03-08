def MinWindowSubstring(strArr: list[str]):
    n = strArr[0]
    k = strArr[1]
    dn, dk = {}, {}
    i, j = 0, len(n) - 1
    best_low, best_high = i, j

    for ch in k:
        dk.setdefault(ch, 0)
        dk[ch] += 1

    for ch in n:
        if ch not in dk:
            continue
        dn.setdefault(ch, 0)
        dn[ch] += 1

    # compress from left
    while True:
        if n[i] not in dk:
            i += 1
        elif dn[n[i]] > dk[n[i]]:
            dn[n[i]] -= 1
            i += 1
        elif dn[n[i]] == dk[n[i]]:
            best_low = i
            break

    # compress from right
    while True:
        if n[j] not in dk:
            j -= 1
        elif dn[n[j]] > dk[n[j]]:
            dn[n[j]] -= 1
            j -= 1
        elif dn[n[j]] == dk[n[j]]:
            best_high = j
            break

    return n[best_low:best_high+1]

# keep this function call here
# print(MinWindowSubstring(input()))


print(MinWindowSubstring(["ahffaksfajeeubsne", "jefaa"]))
