class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}


        for i,v in enumerate(nums):
            remain = target-v
           
            if remain in hmap:
                return [hmap[remain],i]
            else:
                hmap[v]=i
        