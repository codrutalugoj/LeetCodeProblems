# https://leetcode.com/problems/generate-parentheses/
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # recursive solution
        # base case: n open parentheses, n close parentheses
        # add a close parenthesis only if #close < #open 
        stack = []
        out = []

        def backtrack(openN, closedN):
            # base case:
            if openN == closedN == n:
                out.append("".join(stack))
                return
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                # we also need to pop the last parenthesis we added since 
                # the stack is a global variable
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return out

