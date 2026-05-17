class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stackInverses={')':'(',']':'[','}':'{'}
        for bracket in s:
            if bracket in ['(','{','[']:
                stack.append(bracket)
            else:
                if len(stack)==0:
                    return False
                top = stack.pop()
                if top == stackInverses[bracket]:
                    continue
                else:
                    return False
        if len(stack)==0:
            return True
        return False