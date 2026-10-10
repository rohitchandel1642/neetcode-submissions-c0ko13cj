class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prsr = set()
        for i in nums:
            if i in prsr:
                return True
            prsr.add(i)
        return False