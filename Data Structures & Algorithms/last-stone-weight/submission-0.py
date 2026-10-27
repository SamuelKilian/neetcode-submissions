class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        nombres_tries = sorted(stones, reverse=True)
        while len(nombres_tries) >= 2:
            reste = nombres_tries[0] - nombres_tries[1]
            if reste > 0:
                nombres_tries.append(reste)
            nombres_tries.pop(0)
            nombres_tries.pop(0)
            nombres_tries.sort(reverse=True)
        return nombres_tries[0] if nombres_tries else 0 

        