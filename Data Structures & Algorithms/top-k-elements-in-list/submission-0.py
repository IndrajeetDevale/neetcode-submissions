import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap_a = {}

        for n in nums:
            hashmap_a[n] = hashmap_a.get(n, 0) + 1
        
        return heapq.nlargest(k, hashmap_a.keys(), key=lambda x: hashmap_a[x])

        