# Time Complexity : O(N) where N is the length of the input list
# Space Complexity : O(1) 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach:
# I am using bit manipulation to find the unique number in the list where every other number appears twice.
# I initialize a result variable to 0 and iterate through each number in the list,
# performing an XOR operation between the result and the current number.
# Since XORing a number with itself results in 0 and XORing with 0 results in the number itself,
# all the duplicate numbers will cancel each other out, leaving only the unique number in the result.
# Finally, I return the result which contains the unique number.

from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res
        
        