class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            remain = target-nums[i]
            if remain in hmap:
                return [hmap[remain],i]
            hmap[nums[i]]=i