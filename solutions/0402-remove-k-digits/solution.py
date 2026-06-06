class Solution:
    def removeKdigits(self, num: str, k: int) -> str:

        stack=[]
        for i in num:
            while k>0 and stack and stack[-1]>i:
                stack.pop()
                k-=1
            stack.append(i)
        while k>0:
            stack.pop()
            k-=1
        result="".join(stack).lstrip('0')
        if result=="":
            return "0"
        else:
            return result
        # return result if result else "0"

