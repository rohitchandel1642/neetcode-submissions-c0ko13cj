class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        listOfNum=[]
        for i in nums:
            if i in listOfNum:
                return True
            listOfNum.append(i)
        return False
