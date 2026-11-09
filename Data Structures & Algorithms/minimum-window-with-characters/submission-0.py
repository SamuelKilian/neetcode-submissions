class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #comptage de référence
        if not t or not s:
            return ""
        dict_t = dict()
        for c in t:
            dict_t[c] = dict_t.get(c, 0) + 1
        required = len(dict_t)
        #extension de la fenetre 
        window_counts = dict()
        left = 0
        formed = 0

        #stocker meilleur resultat
        ans = (float("inf"), None, None)

        for right, c in enumerate(s):
            window_counts[c] = window_counts.get(c, 0) + 1
            if c in dict_t and window_counts[c] == dict_t[c]:
                formed += 1

        #contraction de la fenetre 
            while left <= right and formed == required:
                if (right - left + 1) < ans[0]:
                    ans = (right - left + 1, left, right)
                left_char = s[left]
                window_counts[left_char] -= 1 
        #mémorisation et le résultat
                if left_char in dict_t and window_counts[left_char] < dict_t[left_char]:
                    formed -= 1
                left += 1

        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]



