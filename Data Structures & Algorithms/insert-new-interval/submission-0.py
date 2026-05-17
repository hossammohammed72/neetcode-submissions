class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        newIntervals = [newInterval]
        for i in range(len(intervals)):
            if newIntervals[len(newIntervals)-1][0] > intervals[i][1]:
                topInterval = newIntervals.pop()
                newIntervals.append(intervals[i])
                newIntervals.append(topInterval)
            elif newIntervals[len(newIntervals)-1][0] <=  intervals[i][1] and newIntervals[len(newIntervals)-1][1] >=  intervals[i][0] :
                newIntervals[len(newIntervals)-1] =[min(intervals[i][0],newIntervals[len(newIntervals)-1][0]),max(newIntervals[len(newIntervals)-1][1],intervals[i][1])]
            elif intervals[i][0] > newIntervals[len(newIntervals)-1][1]:
                newIntervals.append(intervals[i]) 
        return newIntervals
