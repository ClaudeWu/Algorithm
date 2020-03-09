# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Example 2:
#
# Input: "cbbd"
# Output: "bb"

class Solution(object):
    def __init__(self):
        self.longestSize = 0
        self.longestStart = 0

    def longestPalindrome(self, s):
        for index, value in enumerate(s):
            self.checkOddPalindrome(s, index)
            self.checkEvenPalindrome(s, index)
        return s[self.longestStart: self.longestStart + self.longestSize + 1]

    def checkOddPalindrome(self, s, index):
        start = index  # create start value
        end = index  # create end value
        while start >= 1 and end < len(s) - 1 and s[start - 1] == s[end + 1]:  # ensure two index are not at very end
            # and start of two list
            start -= 1
            end += 1
        if end - start > self.longestSize:
            self.longestSize = end - start
            self.longestStart = start

    def checkEvenPalindrome(self, s, index):
        start = index
        end = min(index + 1, len(s) - 1)
        while start >= 1 and end < len(s) - 1 and s[start - 1] == s[end + 1] and s[start] == s[end]:
            start -= 1
            end += 1
        if end - start > self.longestSize and s[start] == s[end]:  # store the length if the result bigger then
            # current length and start = end
            self.longestSize = end - start
            self.longestStart = start


def execute():
    sol = Solution()
    print(sol.longestPalindrome("babbad"))

execute()
