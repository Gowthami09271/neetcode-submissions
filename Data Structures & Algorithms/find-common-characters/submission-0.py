class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        first = words[0]

        for ch in set(first):
            min_count = first.count(ch)

            for word in words:
                count = word.count(ch)

                if count < min_count:
                    min_count = count

            for i in range(min_count):
                res.append(ch)

        return res