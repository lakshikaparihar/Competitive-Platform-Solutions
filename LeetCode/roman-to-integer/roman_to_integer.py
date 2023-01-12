class Solution:
    def romanToInt(self, s: str) -> int:
        dict = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num = 0
        for i in range(len(s)):
            if i==len(s)-1:
                nex=0
            else:
                nex=dict[s[i+1]]
            cur = dict[s[i]]
            if cur<nex:
                num=num-cur
            else:
                num=num+cur
        return num
