class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        first_upper = [-1] * 26
        last_lower = [-1] * 26
        
        for i, char in enumerate(word):
            idx = ord(char.lower()) - ord('a')
            
            if char.islower():
             
                last_lower[idx] = i
            else:
               
                if first_upper[idx] == -1:
                    first_upper[idx] = i
        
        count = 0
        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != -1:
                if last_lower[i] < first_upper[i]:
                    count += 1
                    
        return count
