class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = dict()
        for element in strs:
            s_sorted = "".join(sorted(element))
            if s_sorted not in result:
                result[s_sorted] = []
            result[s_sorted].append(element)

        return list(result.values())
            
        
            