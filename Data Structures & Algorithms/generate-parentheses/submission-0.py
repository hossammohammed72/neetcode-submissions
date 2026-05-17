class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        bracketsList = []
        self.insertParenthesis(n,"",0,0,bracketsList) 
        return bracketsList
    def insertParenthesis(self,n,combination:str,numBracketsOpen:int,numBracketsClosed:int,
    bracketsList:List[str]):
        print(numBracketsOpen,numBracketsClosed,n)
        if numBracketsClosed ==n:
            bracketsList.append(combination)
            return
        if numBracketsOpen < n:
            combination = combination+'('
            self.insertParenthesis(n,combination,numBracketsOpen+1,numBracketsClosed,bracketsList) 
            combination = combination[0:len(combination)-1]
        if numBracketsClosed < numBracketsOpen:
            combination = combination+')'
            self.insertParenthesis(n,combination,numBracketsOpen,numBracketsClosed+1,bracketsList) 

        
