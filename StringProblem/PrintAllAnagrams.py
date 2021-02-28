a = ['cat', 'act', 'man', 'nam', 'god']


def printAnagrams(a):
    a.sort()
    for i in range(len(a)):
        word1 = sorted(list(a[i]))
        for j in range(i + 1, len(a)):
            word2 = sorted(list(a[j]))
            if word1 == word2:
                print(a[i], "   ", a[j])


printAnagrams(a)
