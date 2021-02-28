s = "mamad"


def PallindromePossibleOrNot(s):
    d = dict()
    for i in s:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] = d.get(i) + 1

    return len([key for key, value in d.items() if value % 2 == 1]) <= 1


print(PallindromePossibleOrNot(s))
