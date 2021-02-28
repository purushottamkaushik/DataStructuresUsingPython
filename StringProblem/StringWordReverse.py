def reverseWords(s):
    lst = s.split()
    reverse = []
    for i in lst[::-1]:
        reverse.append(i)

    reversedString = ' '.join(reverse)
    print(reversedString)


s = "I love you sonia"
reverseWords(s)
