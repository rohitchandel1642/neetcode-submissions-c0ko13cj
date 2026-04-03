class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listOfNums={}
        for i in range(0,len(nums)):
            remainder=target-nums[i]
            if remainder in listOfNums:
                return [listOfNums[remainder],i]
            listOfNums[nums[i]]=i
        