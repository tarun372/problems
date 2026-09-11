class Solution:
    def maxNumberOfBalloons(self, text):
        count = [0] * 26

        for c in text:
            count[ord(c) - ord('a')] += 1

        return min(
            count[ord('b') - ord('a')],
            count[ord('a') - ord('a')],
            count[ord('l') - ord('a')] // 2,
            count[ord('o') - ord('a')] // 2,
            count[ord('n') - ord('a')]
        )