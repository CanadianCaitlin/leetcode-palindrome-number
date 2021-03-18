# Link to Leetcode Problem: https://leetcode.com/problems/palindrome-number/
# Difficulty: Easy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reverse_x = []
        for char in str_x:
            reverse_x.insert(0, char)
        if str_x == "".join(reverse_x):
            return True
        return False