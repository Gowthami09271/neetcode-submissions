class Solution:
    def maxDifference(self, s: str) -> int:
        count = {}

        # Count frequencies
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        max_odd = 0
        min_even = float('inf')

        # Find maximum odd and minimum even frequency
        for value in count.values():
            if value % 2 == 1:
                max_odd = max(max_odd, value)
            else:
                min_even = min(min_even, value)

        return max_odd - min_even