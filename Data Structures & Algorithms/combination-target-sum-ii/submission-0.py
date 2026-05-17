class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        memo = []
        momo = {}
        visited = [False]*len(candidates)
        def dfs(target,canlist):
            if target ==0:
                print(canlist)
                canlist = sorted(canlist)
                index = ''
                for item in canlist:
                    index+=str(item)
                if index not in momo:
                    memo.append(canlist)
                    momo[index] = True
                return 
            for i in range(len(candidates)):
                candidate = candidates[i]
                if target-candidate >= 0 and visited[i] == False:
                    newList = []
                    newList[:] = canlist[:]
                    newList.append(candidate)
                    visited[i] = True
                    dfs(target-candidate,newList)
                    visited[i] = False
        dfs(target,[])
        return memo
        

        