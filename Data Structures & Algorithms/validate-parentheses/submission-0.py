class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')' : '(', ']' : '[', '}' : '{'}
        for char in s: # pour chacun des char 
            if char in mapping: #si on le retrouve dans mapping
                if not stack or stack[-1] != mapping[char]: #si stack vide ou dernier élement
                #correspond pas, en gros le dernier ouvert doit etre fermé 
                    return False
                stack.pop()
            else: #il faut mettre un else 
                stack.append(char)
        return len(stack) == 0
        