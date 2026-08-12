class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}

        # Count frequency of each string
        for word in arr:
            count[word] = count.get(word, 0) + 1

        # Find the kth distinct string
        for word in arr:
            if count[word] == 1:
                k -= 1
                if k == 0:
                    return word

        return ""