class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s=set()
        
        while n!=1:
            if n in s:
                return False
            s.add(n)
            total =0
            while n>0:
                d=n%10
                total+=d*d
                n//=10
            n=total
        return True
