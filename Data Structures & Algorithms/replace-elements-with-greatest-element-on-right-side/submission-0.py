class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)

        for i in range(n):
            if i == n - 1:
                arr[i] = -1
            else:
                maxi = arr[i + 1]
                for j in range(i + 1, n):
                    if arr[j] > maxi:
                        maxi = arr[j]
                arr[i] = maxi

        return arr