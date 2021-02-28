

def StringBreak(s,d):

    dp = [ 0 for j in range(len(s) + 1)]
    dp[0] = True
    for i in range(1,len(s)+1):
        for j in range(0,i):
            if dp[j] and s[j:i] in d:
                dp[i] = True
                print("True")
                break

    if True in dp:
        return True
    else:
        return False



if __name__=="__main__":
    s = "helloworld"
    d = {'h','e','he','ll','world'}
    print(type(d))
    print(StringBreak(s,d))