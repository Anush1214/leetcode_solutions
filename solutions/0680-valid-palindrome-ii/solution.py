class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1
        var=1

        while i<j:
            if s[i]==s[j]:
                i+=1
                j-=1
            elif var==1:
                var-=1
                nl=s[:i]+s[i+1:]
                res=nl[::-1]
                if nl==res:
                    return True
                
                nr=s[:j]+s[j+1:]
                res=nr[::-1]
                if nr==res:
                    return True
                else:
                    return False
        return True
