class Evaluation:
    def __init__(self):
        self.stack = []

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return "dddd"

    def push(self, data):
        self.stack.append(data)

    def isEmpty(self):
        return self.stack == []

    def evalexp(self, exp):
        if len(exp) == 0:
            print("There is no expression to evaluate")
            return

        for c in exp:
            if c.isalnum():
                self.push(c)
            elif c == '+':
                self.push(int(self.pop()) + int(self.pop()))

            elif c == '-':
                self.push(int(self.pop()) - int(self.pop()))
            elif c == '*':
                self.push(int(self.pop()) * int(self.pop()))
            else:
                self.push(int(self.pop()) / int(self.pop()))

        return self.pop()


if __name__ == "__main__":
    evaluate = Evaluation()
    res = evaluate.evalexp("234*6*+")
    print(res)
