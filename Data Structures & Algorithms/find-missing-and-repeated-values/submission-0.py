class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        repeat = 0
        n = len(grid)

        # Find repeated number
        for row in grid:
            for num in row:
                if num in seen:
                    repeat = num
                else:
                    seen.add(num)

        # Find missing number
        for i in range(1, n * n + 1):
            if i not in seen:
                return [repeat, i]