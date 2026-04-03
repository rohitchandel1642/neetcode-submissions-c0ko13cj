class Solution:
    def isValid(self, s: str) -> bool:
        hmap = {'}':'{',')':'(',']':'['}
        stck=[]
        for i in s:

            if stck and stck[-1]==hmap.get(i,0):
                stck.pop()
            else:
                stck.append(i)
        return True if not stck else False
        

        