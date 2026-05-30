class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        min=-2**31
        max=2**31-1

        sign=-1 if x<0 else 1
        x=abs(x)

        rev=0
        while x>0:
            dig=x%10
            x//=10

            if rev>max//10 or (rev==max//10 and dig>7):
                return 0

            rev=dig+rev*10
        return sign*rev
        
