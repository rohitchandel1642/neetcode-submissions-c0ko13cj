class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stck=[]
        for i,t in enumerate(temperatures):
            while stck and t>stck[-1][1]:
                stckInd,stckT=stck.pop()
                res[stckInd]=i-stckInd
            stck.append([i,t])
        return res
        
