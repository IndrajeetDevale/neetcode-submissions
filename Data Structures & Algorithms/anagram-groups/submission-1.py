class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap_a = {}
        for s in strs:
            char_map = [0] * 26
            for char in s:
                char_map[ord(char)-ord('a')] += 1
            
            key = tuple(char_map)
            if hashmap_a.get(key):
                hashmap_a[key].append(s)
            else:
                hashmap_a[key] = [s]
        
        res_array = []
        for key, value in hashmap_a.items():
            res_array.append(value)

        return res_array

        