class InfixToPostfixConversion:
    def __init__(self):
        self.stack = []
        self.result = []
        self.precedence = {'(':0,'+':1,'-':1,'*':2,'/':2,'^':3}

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1];

    def isEmpty(self):
        return self.stack == []

    def notgreater(self,c):
        try:
            a = self.precedence[self.peek()]
            b = self.precedence[c]
            return True if a>=b else False
        except KeyError:
            return False



    def infixtopostfix(self,exp):
        for c in exp:
            if c.isalnum():
                self.result.append(c)
            elif c =='(':
                self.stack.append(c)
            elif c ==')':
                x = self.stack.pop()
                while x !='(':
                    self.result.append(x)
                    x = self.stack.pop()
            else:
                while (not self.isEmpty() and self.notgreater(c)):
                    self.result.append(self.stack.pop())
                self.push(c)

        if not self.isEmpty():
            self.result.append(self.pop())

        res = "".join(self.result)
        return res

conversion = InfixToPostfixConversion()
res = conversion.infixtopostfix("(2+3*2+(5-6))")
print(res)


