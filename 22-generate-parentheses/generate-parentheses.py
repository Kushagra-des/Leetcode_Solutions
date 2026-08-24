class Solution:
    def generateParenthesis(self, n: int):
        ans = []

        def backtrack(current, open, close):

            # We have used all 2n brackets
            if open == n and close == n:
                ans.append(current)
                return

            # Add an opening bracket
            if open < n:
                backtrack(current + "(", open + 1, close)

            # Add a closing bracket only if it is valid
            if close < open:
                backtrack(current + ")", open, close + 1)

        backtrack("", 0, 0)

        return ans