class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = {}
        longestSubSequent = 0
        maxSubSequent=0
        lastOccurence=0
        for i in range(0,len(s)):    
            if s[i] in lookup:
                if maxSubSequent < longestSubSequent:
                    maxSubSequent = longestSubSequent
                if lastOccurence < lookup[s[i]]:
                    lastOccurence=lookup[s[i]]
                longestSubSequent=i-lastOccurence
            else:
                longestSubSequent+=1
            lookup[s[i]]=i
        if maxSubSequent < longestSubSequent:
            maxSubSequent = longestSubSequent
        return maxSubSequent
