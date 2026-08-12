class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        res = sorted(set(nums))

        longest = 1
        count = 1

        for i in range(1, len(res)):
            if res[i] == res[i - 1] + 1:
                count += 1
            else:
                longest = max(longest, count)
                count = 1

        longest = max(longest, count)
        return longest