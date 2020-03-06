# There are two sorted arrays nums1 and nums2 of size m and n respectively.
# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# You may assume nums1 and nums2 cannot be both empty.
#
# Example 1:
#
# nums1 = [1, 3]
# nums2 = [2]
# The median is 2.0

# Example 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1) # create m sign with length of num1
        n = len(nums2) # create n sign with length of num2
        if m > n: # ensure the first number always bigger then the second number, long first, short behind
            nums1, nums2, m, n = nums2, nums1, n, m
        if m == 0:
            if n % 2 == 0:
                return nums2[int(n / 2) - 1] + nums2[int(n / 2)] / 2.0
            else:
                return nums2[int(n / 2)]
        iMin = 0
        iMax = m
        half = int((m + n + 1) / 2)
        while iMin <= iMax:
            i = int((iMin + iMax) / 2)
            j = half - i
            if  i < m and nums2[j - 1] > nums1[i]:
                iMin = i + 1
            elif i > 0 and nums1 [i -1] > nums2[j]:
                iMax = i -1
            else:
                if i == 0:
                    maxLeft = num2[j - 1]
                elif j == 0:
                    maxLeft = nums1[i - 1]
                else:
                    maxLeft = max(nums1[i - 1], nums2[j - 1])
                if i == m:
                    minRight = nums2[j]
                elif j == n:
                    minRight = nums1[i]
                else:
                    minRight = min(nums1[i], nums2[j])

                if (m + n) % 2 == 0:
                    return (maxLeft + minRight) / 2.0
                else:
                    return maxLeft

def execute():
    sol = Solution()
    nums1 = []
    nums2 = [2, 3]
    print(sol.findMedianSortedArrays(nums1, nums2))

if __name__ == "__main__":
    execute()