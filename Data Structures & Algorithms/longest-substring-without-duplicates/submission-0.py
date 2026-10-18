class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_seq = 0
        start = 0
        char_set = set()
        for end in range(len(s)):
            while s[end] in char_set:
                char_set.remove(s[start])
                start += 1
            char_set.add(s[end])
            max_seq = max(max_seq, end - start + 1)
        return max_seq            