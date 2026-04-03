class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck=[]

        for i in tokens:
            
            if i =='+':
                b=stck.pop()
                a=stck.pop()
                stck.append(a+b)

            elif i =='-':
                b=stck.pop()
                a=stck.pop()
                stck.append(a-b)
            elif i =='*':
                b=stck.pop()
                a=stck.pop()
                stck.append(a*b)
            elif i =='/':
                print(stck)
                b=stck.pop()
                a=stck.pop()
                print(b,a)
                stck.append(int(float(a)/b))
            else:
                stck.append(int(i))
        return stck[0]