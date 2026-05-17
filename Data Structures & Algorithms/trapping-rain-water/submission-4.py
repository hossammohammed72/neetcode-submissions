class Solution:
    def trap(self, height: List[int]) -> int:
        biggerBarToTheRight = self.getBiggerBartoTheRight(height,0)
        biggerBarToTheLeft=0 
        area = 0 
        for i in range(len(height)):
            if height[i] >= biggerBarToTheRight:
                biggerBarToTheRight = self.getBiggerBartoTheRight(height,i)
            if  min(biggerBarToTheLeft,biggerBarToTheRight)-height[i] >0:
                area+= min(biggerBarToTheLeft,biggerBarToTheRight)-height[i]
            print(biggerBarToTheLeft,biggerBarToTheRight,height[i],min(biggerBarToTheLeft,biggerBarToTheRight)-height[i])
            if height[i] > biggerBarToTheLeft:
                biggerBarToTheLeft = height[i]

        return area
    def getBiggerBartoTheRight(self, height: List[int],current)->int:
        biggerToTheRight=0
        for i in range(current+1,len(height)):
            if height[i] > biggerToTheRight:
                biggerToTheRight = height[i]
        return biggerToTheRight


        