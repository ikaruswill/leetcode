class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lens = len(nums)
        for i in range(lens):
            r = target - nums[i]
            if r in nums[i+1:]:
                return [i,nums[i+1:].index(r)+i+1]
            
        