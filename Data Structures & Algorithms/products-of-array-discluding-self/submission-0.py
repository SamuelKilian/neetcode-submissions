class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = list()
        left.append(1)
        for i in range(len(nums) - 1):
            left.append(left[-1] * nums[i])
        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            #On calcule le résultat final pour la case i en combinant gauche et
            # droite
            left[i] = left[i] * right_product
            #On met à jour le produit de droite pour le prochain tour en le 
            #multipliant par nums[i]
            right_product = right_product * nums[i]

        return left

            
        