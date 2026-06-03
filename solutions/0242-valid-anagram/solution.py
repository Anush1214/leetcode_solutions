class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        
        ds={}
        dt={}

        for i in s:
            ds[i]=ds.get(i,0)+1
        
        for i in t:
            dt[i]=dt.get(i,0)+1

        return ds==dt
