class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        bank1, bank2 = {}, {}
        for i in range(len(s)):
            bank1[s[i]] = 1 + bank1.get(s[i],0)
            bank2[t[i]] = 1 + bank2.get(t[i],0)
        return bank1 == bank2