class Solution(object):
    def toGoatLatin(self, sentence):
        """
        :type sentence: str
        :rtype: str
        """
        vowels="aeiouAEIOU"
        s=sentence.split()
        c=1
        res=[]
        for i in range(len(s)):
            word=s[i]
            if word[0] in vowels:
                res.append(word+"ma"+'a'*c)
                c+=1
            else:
                res.append(word[1:]+word[0]+"ma"+'a'*c)
                c+=1
        return " ".join(res)


        
        
