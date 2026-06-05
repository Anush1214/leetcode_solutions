class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for i in s:
            if st and abs((ord(st[-1])-ord(i)))==32:
                    st.pop()
            else:
                st.append(i)
        return "".join(st)

