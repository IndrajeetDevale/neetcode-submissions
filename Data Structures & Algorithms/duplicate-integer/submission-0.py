class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_ = {}
        for num in nums:
            if num in hash_.keys():
                return True
            hash_[num] = 1
        return False
        