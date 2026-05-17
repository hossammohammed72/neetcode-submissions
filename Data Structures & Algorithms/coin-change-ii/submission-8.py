class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        pathMemo = {}
        coins.sort()
        memo = [[-1] * (amount + 1) for _ in range(len(coins) + 1)]
        self.counter = 0 
        def dfs(amount,i):
            if amount ==0:
                return 1
            if i >=len(coins):
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]
            val=0 
            if amount-coins[i] >= 0: 
                val =  dfs(amount,i+1)
                val+= dfs(amount-coins[i],i)
            memo[i][amount] = val
            return val
        return dfs(amount,0)
        