
def factorial (num) :
    if num == 0 or num ==1 :
        return 1
    else :
        return num * factorial(num-1)

if __name__=="__main__":
    fact = factorial(5)
    print(fact)