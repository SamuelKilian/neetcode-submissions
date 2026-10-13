class Solution:

    def encode(self, strs: List[str]) -> str:
        resultat = ""
        for s in strs:
            #On met un str() car on veut un chiffre en string, c'est int par defaut
            # on met += au lieu de = pour pas écraser le 1er mot
            resultat += str(len(s)) + "#" + s
        return resultat

    def decode(self, s: str) -> List[str]:
        # liste vide
        resultat = list()
        #index a 0
        i = 0
        # si s vaut 7 , tant que i < 7 
        while i < len(s):
            #on met à chaque fois j = 1 puis j = 2 etc
            j = i
            #on cherche avec un autre index "#"
            while j < len(s) and s[j] != "#":
                j += 1
            #une fois qu'on a j = 3 là où on a le #
            # donc i:j i à l'indice pile avant j
            size_word = int(s[i:j])
            word = s[j + 1 : j + 1 + size_word]
            resultat.append(word)
            #On passe au mot suivant
            # j est au # du premier mot, on met +1 pour l'indice du 1er mot
            # et size pour sauter le mot entier, et on continue
            i = j + 1 + size_word
        return resultat

