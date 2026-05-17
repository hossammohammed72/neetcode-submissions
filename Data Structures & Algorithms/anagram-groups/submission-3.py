class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angramsList = defaultdict(list)
        for string in strs:
            frequency_hash=[0]*26
            for char in string:
                frequency_hash[ord(char)-ord('a')] += 1
            if tuple(frequency_hash) in angramsList:
                angramsList[tuple(frequency_hash)].append(string)
            else:
                angramsList[tuple(frequency_hash)] = [string]
        return list(angramsList.values())
        