class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dfs(i,sequence):
            if i >= len(nums):
                return 0  
            first = 0 
            print(i,sequence)
            if i+1 not in sequence and i-1 not in sequence:
                newSequence = []
                newSequence[:] = sequence[:]
                newSequence.append(i)
                first = nums[i]+dfs(i+1,newSequence)
            if i in memo:
                return max(first,memo[i])
            second = dfs(i+1,sequence)
            memo[i] = second
            return max(first,second)
        
        return dfs(0,[])