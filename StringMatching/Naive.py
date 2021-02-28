s = 'aabaacaadaabbaabb'
p = 'caad'

def detectpattern(s,p):
    n = len(s)
    m = len(p)

    for i in range(n-m +1):
        j =0
        while j < m:
            if s[i+j] != p[j]:
                break
            j +=1
        if j == m:
            print("pattern Found at index {}".format(i))


detectpattern(s,p)
