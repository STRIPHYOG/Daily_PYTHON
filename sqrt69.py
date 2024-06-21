 # Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
    # The returned integer should be non-negative as well.
    # You must not use any built-in exponent function or operator.
    #
    # Example 1:
    # Input: x = 4
    # Output: 2
    # Explanation: The square root of 4 is 2, so we return 2.
    #
    # Example 2:
    # Input: x = 8
    # Output: 2
    # Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
    #
    # Constraints:
    # 0 <= x <= 2^31 - 1

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

def main():
    solution = Solution()
    test_cases = [4, 8, 0, 1, 9, 15, 16]
    for x in test_cases:
        print(f"The square root of {x} is {solution.mySqrt(x)}")

if __name__ == "__main__":
    main()
