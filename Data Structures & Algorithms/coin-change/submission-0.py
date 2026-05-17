class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)
        if amount == 0:
            return 0
        if amount < coins[0]:
            return -1
        memoization = {}
        def getMinCoins(amount):
            if amount == 0:
                return 0
            if amount in memoization:
                return memoization[amount]
            res = 1e9
            for coin in coins:
                if amount-coin>=0:
                    res = min(res,1+getMinCoins(amount-coin))        
            memoization[amount]=res
            return res
        minCoins = getMinCoins(amount)  
        return -1 if minCoins >= 1e9 else minCoins
