class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for i in nums:
            counter[i]=1+counter.get(i,0)
        
        res = [[] for i in range(len(nums)+1)]
        
        for i in counter.keys():
            res[counter[i]].append(i)
            
        finl=[]
        for i in range(len(res)-1,0,-1):
            for j in res[i]:
                finl.append(j)
                if len(finl)==k:
                    return finl
      