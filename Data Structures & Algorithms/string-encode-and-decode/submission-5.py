import re
class Solution:

    def encode(self, strs: List[str]) -> str:
        output= ''
        if len(strs) ==0:
            return '-'
        for string in strs:
            output+=string+'-'
        output = output[0:len(output)-1]
        
        return output 


    def decode(self, s: str) -> List[str]:
        if s =='-':
            return []
        return re.split('-',s)
