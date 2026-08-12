class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}

        for num in arr:
            count[num] = count.get(num, 0) + 1

        ans = -1

        for key, val in count.items():
            if key == val:
                ans = max(ans, key)

        return ans