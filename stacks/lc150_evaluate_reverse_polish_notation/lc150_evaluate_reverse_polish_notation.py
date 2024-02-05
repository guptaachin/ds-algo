from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token == "+":
                b = stk.pop(-1)
                a = stk.pop(-1)
                stk.append(a + b)
            elif token == "-":
                b = stk.pop(-1)
                a = stk.pop(-1)
                stk.append(a - b)
            elif token == "*":
                b = stk.pop(-1)
                a = stk.pop(-1)
                stk.append(a * b)
            elif token == "/":
                b = stk.pop(-1)
                a = stk.pop(-1)
                stk.append(int(a / b))
            else:
                stk.append(int(token))

        return stk.pop(-1)
