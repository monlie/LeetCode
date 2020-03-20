class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        lis = [0] * len(s)
        dp = [0] * len(s)
        for idx, char in enumerate(s):
            if stack and char == ")":
                last, lpos = stack[-1]
                if last == "(":
                    stack.pop()
                    lis[idx] = idx - lpos
            else:
                stack.append((char, idx))
            dis = lis[idx]
            if dis > 0:
                dp[idx] = dis + 1
                if idx - dis - 1 >= 0 and dp[idx - dis - 1] > 0:
                    dp[idx] += dp[idx - dis - 1]
        return max(dp)
