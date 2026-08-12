class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ran_count = {}
        mag_count = {}

        # Count characters in ransomNote
        for ch in ransomNote:
            ran_count[ch] = ran_count.get(ch, 0) + 1

        # Count characters in magazine
        for ch in magazine:
            mag_count[ch] = mag_count.get(ch, 0) + 1

        # Compare counts
        for ch in ran_count:
            if ran_count[ch] > mag_count.get(ch, 0):
                return False

        return True