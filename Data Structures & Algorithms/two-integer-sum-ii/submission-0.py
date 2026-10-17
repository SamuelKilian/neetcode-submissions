class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1 #7
        while left < right:
            current_number = numbers[left] + numbers[right]
            if current_number < target:
                left += 1
            elif current_number > target:
                right -= 1
            else:
                return [left + 1, right + 1]