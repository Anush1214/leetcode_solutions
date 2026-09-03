class Solution:
    def largestOddNumber(self, num: str) -> str:
        # return num.rstrip('02468').lstrip('0')
        length = len(num)
        
        for i in range(length -1 , -1, -1):
            if int(num[i]) % 2 == 1:
                return num[0:i+1]

        return ""
