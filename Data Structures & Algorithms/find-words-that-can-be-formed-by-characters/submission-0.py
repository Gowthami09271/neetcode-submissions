class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = {}

        # Count characters in chars
        for ch in chars:
            char_count[ch] = char_count.get(ch, 0) + 1

        ans = 0

        for word in words:
            word_count = {}
            good = True

            # Count characters in current word
            for ch in word:
                word_count[ch] = word_count.get(ch, 0) + 1

            # Check if word can be formed
            for ch in word_count:
                if word_count[ch] > char_count.get(ch, 0):
                    good = False
                    break

            if good:
                ans += len(word)

        return ans