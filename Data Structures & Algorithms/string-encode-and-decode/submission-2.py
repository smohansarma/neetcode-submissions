class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for word in strs:
            encoded_string = encoded_string+str(len(word))+"#"+word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        i=0
        while(i<len(s)):
            seperator = (s.index("#",i))
            length = int(s[i:seperator])

            start = seperator + 1
            end = start + length
            word = s[start:end]
            decoded_strs.append(word)
            i=end
        return decoded_strs
