class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #on change en set pour enlver les doublons
        #on initialise un longest_streak de base (qui va changer)
        nums_set = set(nums)
        longest_streak = 0
        # pour chaque index, si y'a pas de i - 1, donc ca marque le debut d'un streak
        for i in nums_set:
            if (i - 1) not in nums_set:
                current_number = i
                current_streak = 1
                #tant que y'a le +1 le streak continue, donc on avance de 1 le nombre et
                #le streak       
                while (current_number + 1) in nums_set:
                    current_number += 1
                    current_streak += 1
                #on update au fur et à mesure le longest streak
                longest_streak = max(current_streak, longest_streak)
        #quand on finit on sort du if et on ramène le dernier longest_streak
        return longest_streak

        