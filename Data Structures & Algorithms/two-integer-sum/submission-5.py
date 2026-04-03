class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listNm={}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in listNm:
                return [listNm[remainder],i]
            listNm[nums[i]]=i
        