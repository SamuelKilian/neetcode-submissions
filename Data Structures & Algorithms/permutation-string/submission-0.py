class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False 
        
        compte = dict()
        window_count = dict()
        left = 0


        for c in s1:
            compte[c] = compte.get(c, 0) + 1
        for s in s2[:len(s1)]:
            window_count[s] = window_count.get(s, 0) + 1
        if compte == window_count:
            return True
        for right in range(len(s1), len(s2)):
            # ajouter le nouveau caractère à droite
            c = s2[right]
            window_count[c] = window_count.get(c, 0) + 1

            # retirer l'ancien caractère à gauche
            c = s2[left]
            window_count[c] -= 1

            if window_count[c] == 0:
                del window_count[c]
            left += 1
            # en gros le window prend la taille de s1, on enleve derriere et ajoute devant
            # jusqu'a qu'on ait deux dict similaires
            if compte == window_count:
                return True
        return False 




        