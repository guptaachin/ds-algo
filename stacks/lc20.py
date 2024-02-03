class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_bracket_pairs = {")": "(", 
                              "}": "{",
                              "]": "["}
        for c in s:
            if c in dict_bracket_pairs:
                if len(stack) > 0:
                    last_pushed = stack.pop(-1)
                    if last_pushed != dict_bracket_pairs[c]:
                        return False
                else:
                    return False
            else:
                stack.append(c)
        # the stack has to be empty.
        if len(stack) > 0:
            return False
        return True
