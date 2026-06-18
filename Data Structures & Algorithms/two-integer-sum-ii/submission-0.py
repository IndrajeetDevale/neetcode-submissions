class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a = 0
        b = len(numbers) - 1

        while True:
            sum = numbers[a] + numbers[b]
            if sum == target:
                return [a+1,b+1]
            elif sum > target:
                b -= 1
            else:
                a += 1
        