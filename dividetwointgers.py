# Time Complexity : O(logN) where N is the absolute value of the dividend
# Space Complexity : O(1) 
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach:
# I am using bit manipulation to perform division without using multiplication, division, or mod operator.
# I first handle the edge case where the dividend is INT_MIN and divisor is -1,
# which would cause an overflow. I then take the absolute values of both dividend and divisor.
# I use a while loop to subtract the divisor from the dividend using bit shifts to find the
# largest multiple of the divisor that fits into the dividend. I keep track of the result
# by adding the corresponding power of two for each successful subtraction. 
# Finally, I determine the sign of the result based on the original signs of the dividend and divisor.

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2**31 and divisor == -1:
            return 2**31-1
        ldividend = abs(dividend)
        ldivisor = abs(divisor)

        res = 0
        while ldividend >= ldivisor:
            numshifts = 1
            while (ldivisor << numshifts) <= ldividend:
                numshifts += 1
            numshifts -= 1
            res += 1 << numshifts
            ldividend -= ldivisor << numshifts
        if dividend < 0 and divisor < 0:
            return res
        if dividend < 0 or divisor < 0:
            return -res
        return res


        