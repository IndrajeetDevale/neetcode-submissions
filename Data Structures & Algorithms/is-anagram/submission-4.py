class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap_a = {}
        hashmap_b = {}

        if len(s) != len(t):
            return False
        
        for char in s:
            if char in hashmap_a:
                hashmap_a[char] += 1
            else:
                hashmap_a[char] = 1

        for char in t:
            if char in hashmap_b:
                hashmap_b[char] += 1
            else:
                hashmap_b[char] = 1

        return hashmap_a == hashmap_b
                