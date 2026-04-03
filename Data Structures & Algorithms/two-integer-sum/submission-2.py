class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_series = {}

        for i in range(len(nums)):
            remain = target-nums[i]
            if remain in num_series:
                return [num_series[remain],i]
            else:
                num_series[nums[i]]=i
