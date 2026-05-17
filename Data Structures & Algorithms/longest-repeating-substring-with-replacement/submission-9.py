class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count_map = {}
        res = 0
        biggest_frequency=0
        for r in range(len(s)):
            count_map[s[r]] = 1+count_map.get(s[r],0)
            biggest_frequency = max(biggest_frequency,count_map[s[r]])
            while (r-l+1) -biggest_frequency > k:
               count_map[s[l]]-=1
               l+=1
            res = max(res,r-l+1)
        return res