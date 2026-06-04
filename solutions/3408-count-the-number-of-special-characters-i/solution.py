class Solution(object):
    def numberOfSpecialChars(self, word):
        """
        :type word: str
        :rtype: int
        """
        s=set(word)
        count=0
        l="abcdefghijklmnopqrstuvwxyz"
        for i in l:
            if i in word and i.upper() in s:
                count+=1
        return count
