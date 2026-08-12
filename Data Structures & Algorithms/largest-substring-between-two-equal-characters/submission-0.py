class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res = -1

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    if j - i - 1 > res:
                        res = j - i - 1

        return res