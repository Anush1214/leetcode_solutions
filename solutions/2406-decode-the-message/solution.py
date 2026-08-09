class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        mapping:dict[str,str]={}
        for ch in key:
            if ch!=' ' and ch not in mapping:
                mapping[ch] = chr(ord('a') + len(mapping))
                if len(mapping)==26:
                    break
        return ''.join(mapping[ch] if ch != ' ' else ' ' for ch in message)

