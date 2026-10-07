class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_S={}
        count_T={}
        if len(s) != len(t):
            return False
        for i in s:
            if i in count_S:
                count_S[i] = count_S[i]+1
            else:
                count_S[i]=1

        for j in t:
            if j in count_T:
                count_T[j]= count_T[j]+1
            else:
                count_T[j]=1

        if count_S == count_T:
            return True
        else:
            return False
        