import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap_a = {}

        for n in nums:
            hashmap_a[n] = hashmap_a.get(n, 0) + 1
        
        heap = []
        
        for num, count in hashmap_a.items():
            heapq.heappush(heap, (count, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for count, num in heap]
        