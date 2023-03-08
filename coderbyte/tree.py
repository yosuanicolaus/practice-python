def TreeConstructor(strArr: list[str]):
    d: dict[int, list[int]] = {}

    for word in strArr:
        words = word[1:-1].split(',')
        words = map(int, words)
        child, parent = words
        d.setdefault(parent, [])
        d[parent].append(child)

    for parent, childs in d.items():
        if len(childs) > 2:
            return False
        elif len(childs) == 1:
            continue
        else:
            # have 2 child
            a, b = sorted(childs)
            if a > parent or b < parent:
                return False

    return True


TreeConstructor(["(1,2)", "(2,4)", "(5,7)", "(7,2)", "(9,5)"])
