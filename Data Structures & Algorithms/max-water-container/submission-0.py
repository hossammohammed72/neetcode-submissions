class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i,firstBar in enumerate(heights):
            for j,secondBar in enumerate(heights):
                smallerBar = firstBar
                if secondBar < smallerBar:
                    smallerBar = secondBar
                waterArea = (j-i)*smallerBar
                if waterArea > maxArea:
                    maxArea = waterArea
        return maxArea
        