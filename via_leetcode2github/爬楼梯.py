class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 1
        if n < 2:
            return 1
        for _ in range(n-1):
            a, b = b, a + b
        return b
