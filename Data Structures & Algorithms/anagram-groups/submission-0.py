class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_strings = {}
        for s in strs:
            char_array = [0] * 26
            for c in s:
                numeric_value = ord(c) - ord('a')
                char_array[numeric_value] += 1

            key = tuple(char_array)
            
            if key not in hash_strings:
                hash_strings[key] = []

            hash_strings[key].append(s)

        return list(hash_strings.values())
            
        
