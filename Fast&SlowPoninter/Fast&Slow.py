# 202. Happy Number
# https://leetcode.com/problems/happy-number/description/

# Approach: Repeatedly replace the number with the sum of squares of its digits and store each intermediate result in a list. If the number becomes 1, it is a happy number. If any number repeats, a cycle is detected, meaning it will never reach 1, so return false.
# COMPLEXITY ANALYSIS: Time = O(k²)  Space = O(k)
# class Solution:
#     def sumOfSquareOfDigits(self, n):
#         total = 0
#         while n > 0:
#             dig = n % 10
#             total += dig * dig
#             n //= 10
#         return total

#     def isHappy(self, n: int) -> bool:
#         seen = []
#         while n != 1:
#             if n is seen:
#                 return False
#             seen.append(n)
#             n = self.sumOfSquareOfDigits(n)
#         return True
# Example Walkthrough 
# Input: n = 19
# Step 1:
# seen = []
# n = 19
# Digits: 1, 9
# Sum of squares = 1² + 9² = 82
# seen = [19]
# n = 82
# Step 2:
# n = 82
# Digits: 8, 2
# Sum of squares = 8² + 2² = 68
# seen = [19, 82]
# n = 68
# Step 3:
# n = 68
# Digits: 6, 8
# Sum of squares = 6² + 8² = 100
# seen = [19, 82, 68]
# n = 100
# Step 4:
# n = 100
# Digits: 1, 0, 0
# Sum of squares = 1² = 1
# n = 1
# Final Result: Since the number becomes 1, the function returns True (Happy Number).
