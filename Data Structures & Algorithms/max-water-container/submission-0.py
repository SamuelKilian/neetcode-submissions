class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #1 Initialisation
        left = 0
        right = len(heights) - 1
        current_max = 0
        #2 Boucle principale
        while left < right:
            distance = right - left #difference d'indices pas d'hauteurs
            height = min(heights[right], heights[left])
            area = distance * height
            current_max = max(current_max, area) #area et pas height

            if heights[left] < heights[right]:
                left += 1
            else: #au lieu de elif si y'a égalité
                right -=1

        return current_max
         