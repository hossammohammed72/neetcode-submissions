class KthLargest:
    sorted_nums = []
    bar = 1
    def __init__(self, k: int, nums: List[int]):
        self.sorted_nums = sorted(nums)
        self.bar = k

    def add(self, val: int) -> int:
        for i in range(len(self.sorted_nums)):
            if self.sorted_nums[i] > val:
                temp = self.sorted_nums[i]
                self.sorted_nums[i] = val
                val = temp
        self.sorted_nums.append(val)
        res = self.sorted_nums[len(self.sorted_nums)-self.bar]
        return res
