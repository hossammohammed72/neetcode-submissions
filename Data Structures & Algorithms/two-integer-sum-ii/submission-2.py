class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for j,num1 in enumerate(numbers):
            for i,num2 in enumerate(numbers):
                if num1+num2 == target:
                    return [j+1,i+1]
        