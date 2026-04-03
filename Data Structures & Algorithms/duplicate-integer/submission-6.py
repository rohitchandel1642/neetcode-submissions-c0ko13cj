class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list_of_num = []
        for i in range(0,len(nums)):
            if nums[i] in list_of_num:
                return True
            list_of_num.append(nums[i])
        return False