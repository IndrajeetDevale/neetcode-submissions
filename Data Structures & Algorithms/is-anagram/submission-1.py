class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashset_s = {}
        for char in s:
            if char in hashset_s:
                hashset_s[char] += 1
            else:
                hashset_s[char] = 1

        hashset_t = {}
        for char in t:
            if char in hashset_t:
                hashset_t[char] += 1
            else:
                hashset_t[char] = 1

        if hashset_t == hashset_s:
            return True
        
        return False
        