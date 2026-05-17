class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        comparisonStr = strs
        angaramList = {}
        for refstr in strs:
            if "".join(sorted(refstr)) in angaramList:
                angaramList["".join(sorted(refstr))].append(refstr)
            else:
                angaramList["".join(sorted(refstr))] = [refstr]
        return angaramList.values() 


        
        