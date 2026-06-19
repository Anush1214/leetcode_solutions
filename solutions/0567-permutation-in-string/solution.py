class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1=len(s1)
        len_s2=len(s2)

        if len_s1>len_s2:
            return False
        
        s1_count= [0]*26
        window= [0]*26

        for i in range(len_s1):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        
        if s1_count==window:
            return True
        for i in range(len_s1,len_s2):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - len_s1]) - ord('a')] -= 1

            if s1_count==window:
                return True
        return False
