class WordDictionary:

    def __init__(self):
        self.trie = {}     

    def addWord(self, word: str) -> None:
        currentNode = self.trie
        for i in range(len(word)):
            if word[i] not in currentNode:
                currentNode[word[i]] = {}
            currentNode = currentNode[word[i]]
        currentNode['*'] = {}
        

    def search(self, word: str) -> bool:
        def traverseTrie(i,word,currentNode):
            if i==len(word) and '*' in currentNode:
                return True
            elif i==len(word):
                return False
            print(i,word,len(word))
            if word[i] == ".":
                value = False
                i+=1
                for key in currentNode:
                    value =  value or traverseTrie(i,word,currentNode[key])  
                return value  
            if word[i] not in currentNode:
                return False
            else:
                currentNode = currentNode[word[i]]
                i+=1
                return traverseTrie(i,word,currentNode)
        return traverseTrie(0,word,self.trie)

        
