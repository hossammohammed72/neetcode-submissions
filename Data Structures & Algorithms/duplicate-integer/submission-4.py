from numpy import zeros
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_numbers = {}
        if len(nums) == 0:
            return False
        for number in nums:
            if number in duplicate_numbers:
                duplicate_numbers[number] += 1 
            else:
                duplicate_numbers[number]=1
        print(duplicate_numbers,max(duplicate_numbers,key=duplicate_numbers.get))
        if duplicate_numbers[max(duplicate_numbers,key=duplicate_numbers.get)] > 1:
            return True
        return False
         