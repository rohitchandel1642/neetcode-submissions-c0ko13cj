class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        res = [[] for i in range(len(nums)+1)]
        
        for i in nums:
            counter[i]=counter.get(i,0)+1
        
        for i in counter:
           
            res[counter[i]].append(i)
        
        k_elemnt=[]
        for i in range(len(res)-1,0,-1):
            for j in res[i]:
                k_elemnt.append(j)
                if len(k_elemnt)==k:
                    return k_elemnt