class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}

        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1

        for i in range(len(s)):
            if d[s[i]] == 1:
                return i

        return -1