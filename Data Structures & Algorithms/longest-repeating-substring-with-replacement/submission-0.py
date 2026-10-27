class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = dict()
        max_freq = 0
        max_len = 0
        for right, char in enumerate(s):
            counts[char] = counts.get(char, 0) + 1
            #On actualise max_freq : est-ce que la lettre qu'on vient 
            # d'ajouter bat le record de fréquence ?
            max_freq = max(max_freq, counts[char])
            # Si ce nombre dépasse notre budget 'k', la fenêtre est trop grande.
            while (right - left + 1 ) - max_freq > k:
                counts[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        return max_len
            