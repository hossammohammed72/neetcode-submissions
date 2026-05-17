class Solution:
    def climbStairs(self, n: int) -> int:

        def dfs(amount):
            if amount == 0:
                return 1
            if amount < 0:
                return 0
            return dfs(amount-1)+dfs(amount-2)
        return dfs(n)

        