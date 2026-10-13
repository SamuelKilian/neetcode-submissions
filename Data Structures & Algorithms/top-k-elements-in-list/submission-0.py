class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #On convertit la liste en dictionnaire pour avoir les frequences
        frequence = dict()
        for num in nums:
            frequence[num] = frequence.get(num, 0) + 1
        #on va trier ce dictionnaire en ordre décroissant
        nums_order = sorted(frequence.items(), key = lambda x: x[1], reverse=True)

        #on a le dictionnaire en ordre, maintenent on cree la liste a retourner
        final_result = []
        for cle, val in nums_order[:k]:
            final_result.append(cle)
        return final_result

        
        