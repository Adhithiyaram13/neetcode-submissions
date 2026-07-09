class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Flag = False
        num_set = set(nums)
        if len(nums) != len(num_set):
            Flag = True
        return Flag
         