# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:

        stack = [] # all open brackets
        matching = { ")": "(", "]": "[", "}": "{"}
        
        for p in s:
            if p in matching:
                if stack and matching[p] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return True if not stack else False
            