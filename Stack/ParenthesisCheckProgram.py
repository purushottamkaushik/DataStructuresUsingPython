class Paranthesis:
    def __init__(self):
        self.stack = []

    def parenthesischeck(self,exp):

        for i in range(len(exp)):
            if exp[i] =='{' or exp[i] == '[' or exp[i] =='(':
                self.stack.append(exp[i])

            if len(self.stack) == 0:
                return False

            if exp[i] == '}':
                ch = self.stack.pop()
                if ch !='{':
                    return False

            if exp[i] == ')':
                ch = self.stack.pop()
                if ch != '(':
                    return False

            if exp[i] == ']':
                ch = self.stack.pop()
                if ch != '[':
                    return False

        if len(self.stack) !=0:
            return False
        else:
            return True

if __name__=="__main__":
    p = Paranthesis()
    str = input("Enter a parenthesis to check")
    if p.parenthesischeck(str):
        print("its a valid parenthesis ")
    else :
        print("Its a invalid paranthesis")