class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stck = []
        for i in range(0,len(temperatures)):
            count = 0
            while count+i<=n-1:
                if temperatures[i]<temperatures[count+i]:
                    break
                count+=1
            count = 0 if count+i>=n else count
            stck.append(count)
        return stck
        
