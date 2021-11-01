class Solution(object):
    def romanToInt(self, s):
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        num = 0
        if len(s)==1:
            return roman[s]
        for i in range(len(s)-1):
            if roman[s[i]] < roman[s[i+1]]:
                num -= roman[s[i]]
            else:
                num += roman[s[i]]
            if i+2 == len(s):
                num += roman[s[i+1]]
        return num