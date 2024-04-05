class Solution:
    def makeGood(self, s: str) -> str:
        stack = list()
        for c in s:
            if len(stack) == 0:
                stack.append(c)
            else:
                if abs(ord(c) - ord(stack[-1])) == 32:
                    stack.pop(-1)
                else:
                    stack.append(c)
        return "".join(stack)
