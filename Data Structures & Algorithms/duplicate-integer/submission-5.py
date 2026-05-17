class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate_numbers = {}
        if len(nums) == 0:
            return False
        for number in nums: 
            if number in duplicate_numbers: 
                return True
            else:
                duplicate_numbers[number] = True
        return False