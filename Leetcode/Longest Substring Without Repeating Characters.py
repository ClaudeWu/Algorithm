# Given a string, find the length of the longest substring without repeating characters.
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
#              Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

class Solution:
    def lengthOfLongestSubstring(self, s):
        tempDict = {} # create a dict to store char and pointer
        maxLen = 0 # crate a value to store max length of string
        pointer = 0 # create a pointer to get each char's index
        for index, value in enumerate(s):
            if value in tempDict:
                pointer = max(tempDict[value] + 1, pointer) # the pointer should not move back, using max() take the maximum value
            maxLen = max(index - pointer + 1, maxLen)# the length should increase but not decrease
            tempDict[value] = index # update dict
        return maxLen

def execute():
    sol = Solution()
    print(sol.lengthOfLongestSubstring("pwwkew"))

if __name__ == "__main__":
    execute()
