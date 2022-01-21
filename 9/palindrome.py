class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False
        revertedNumber = 0
        while (x > revertedNumber):
            revertedNumber = revertedNumber * 10 + x % 10
            x = x // 10
        return (x == revertedNumber or x == revertedNumber // 10)

if __name__ == "__main__":
	print(121, "is a palindrome:", Solution.isPalindrome(Solution, 121))
	print(-121, "is a palindrome:", Solution.isPalindrome(Solution, -121))
	print(10, "is a palindrome:", Solution.isPalindrome(Solution, 10))
	print(11, "is a palindrome:", Solution.isPalindrome(Solution, 11))
