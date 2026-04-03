class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listOfNums={}

        for i in range(len(nums)):
            remainder=target-nums[i]
            
            if remainder in listOfNums.keys():
                return [listOfNums[remainder],i]
            listOfNums[nums[i]]=i
        