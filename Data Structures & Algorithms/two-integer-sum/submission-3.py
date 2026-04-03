class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_hmap={}

        for i in range(len(nums)):
            remain = target-nums[i]
            if remain in num_hmap:
                return [num_hmap[remain],i]
            num_hmap[nums[i]]=i