class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_series={}
        
        for i,v in enumerate(nums):
            remain = target-v
            if remain in num_series:
                return [num_series[remain],i]
            else:
                num_series[v]=i
        return False