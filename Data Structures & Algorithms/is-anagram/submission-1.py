class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
       
        countOne,countTwo={},{}

        for i in range(len(s)):
            countOne[s[i]]=1+countOne.get(s[i],0)
            countTwo[t[i]]=1+countTwo.get(t[i],0)
        
        for i in countOne:
            if countOne[i]!=countTwo.get(i,0):
                return False
        return True

