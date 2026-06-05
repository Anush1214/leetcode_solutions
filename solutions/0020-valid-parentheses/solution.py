class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # st = {')': '(', ']': '[', '}': '{'}
        # stack=[]

        # for ch in s:
        #     if ch in st:
        #         if stack:
        #             top=stack.pop()
        #         else:
        #             return False
        #         if st[ch]!=top:
        #             return False
        #     else:
        #         stack.append(ch)
        # return not stack

        st=[]
        for ch in s:
            if ch=="(":
                st.append(")")
            elif ch=="{":
                st.append("}")
            elif ch=="[":
                st.append("]")
            elif len(st)==0 or st[-1]!=ch:
                return False
            else:
                st.pop()
        return len(st)==0
