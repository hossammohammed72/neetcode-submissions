class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        angramsList = {}
        for string in strs:
            sortedString = str(sorted(string))
            if sortedString in angramsList:
                angramsList[sortedString].append(string)
            else:
                angramsList[sortedString] = [string]
        return list(angramsList.values())
        