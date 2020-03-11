# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to
# display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R

# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);

# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"

# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

class Solution(object):
    def convert(self, s, numRows):
        result = ""
        length = len(s)
        n = numRows
        cycle = 2 * n - 2
        if n == 1:  # if only one row then just return to s
            return s
        i = 0  # set rows
        x = 0  # set cycle numbers
        while len(result) < length:  # when the length of result still less than length of original string
            if cycle * x + i > length - 1:  # if zig value bigger then the length of original string
                i += 1  # row + 1
                x = 0  # cycle become 0
            zig = cycle * x + i
            zag = cycle * (x + 1) - i
            if i == 0 or i == n - 1:  # if only one row
                result += s[zig]  # then we don't need zag value
            else:
                if zag > length - 1:
                    result += s[zig]
                else:
                    result += s[zig] + s[zag]
            x += 1
        return result


def execute():
    sol = Solution()
    print(sol.convert("PAYPALISHIRING", 4))

if __name__ == "__main__":
    execute()
