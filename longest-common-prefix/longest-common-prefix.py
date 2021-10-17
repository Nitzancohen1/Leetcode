class Solution(object):
    def longestCommonPrefix(self, strs):
        i=0
        pref=""
        for letter in strs[0]:
            for word in strs:
                if i==len(word):
                    return pref
                if word[i]!=letter:
                    return pref
            pref+=letter
            i+=1
        return pref
        """
        :type strs: List[str]
        :rtype: str
        """
        