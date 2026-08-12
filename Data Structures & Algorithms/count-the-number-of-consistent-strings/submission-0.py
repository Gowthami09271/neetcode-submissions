class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        count = 0

        for word in words:
            consistent = True

            for ch in word:
                if ch not in allowed_set:
                    consistent = False
                    break

            if consistent:
                count += 1

        return count