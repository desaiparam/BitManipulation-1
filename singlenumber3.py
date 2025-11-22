# Time Complexity : O(N) where N is the length of the input list
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach:
# I am using bit manipulation to find the two unique numbers in the list where every other number appears twice.
# First, I XOR all the numbers in the list to get a combined bitmask of the two unique numbers.
# Then, I find the least significant bit (lsb) that is set in the combined bitmask.
# This lsb helps to differentiate between the two unique numbers.
# I then iterate through the list again, partitioning the numbers into two groups based on whether
# the lsb is set or not, and XORing the numbers in each group to isolate the unique numbers.
# Finally, I return the two unique numbers as a list.
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        bitmask1 = 0
        for i in nums:
            bitmask1 = bitmask1^ i
        bitmask2 = 0
        lsb = bitmask1 & -bitmask1
        for i in nums:
            if (i & lsb ) != 0:
                bitmask2 = bitmask2 ^ i
        return [bitmask2,bitmask1^bitmask2]
        