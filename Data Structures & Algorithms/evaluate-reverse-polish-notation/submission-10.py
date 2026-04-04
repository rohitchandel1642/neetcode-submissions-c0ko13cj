class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stck=[]
        for i in tokens:
            if i =='+' and stck:
                a=stck.pop()
                b=stck.pop()
                
                stck.append(b+a)
            elif i=='-' and stck:
                a=stck.pop()
                b=stck.pop()
                stck.append(b-a)
            elif i=='*' and stck:
                a=stck.pop()
                b=stck.pop()
                stck.append(a*b)
            elif i=='/' and stck:
                a=stck.pop()
                b=stck.pop()
                stck.append(int(b/a))
            else:
                stck.append(int(i))
        return stck[0]

