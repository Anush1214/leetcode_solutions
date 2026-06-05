class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for i in s:
            if st and abs((ord(st[-1])-ord(i)))==0:
                    st.pop()
            else:
                st.append(i)
        return "".join(st)
