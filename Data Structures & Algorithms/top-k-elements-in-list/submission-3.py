class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcnt={}
        for i in nums:
            numcnt[i]=1+numcnt.get(i,0)
        numfreq=defaultdict(list)
        for val,cnt in numcnt.items():
            numfreq[cnt].append(val)
        
        op=[]
        for i in range(len(nums),0,-1):
            if numfreq[i]:
                for j in numfreq[i]:
                    op.append(j)
                if len(op)==k:
                    return op
