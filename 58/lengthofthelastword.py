class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		count = 0
		for i in range(len(s)):
			if (s[-i - 1] == ' ' and count == 0): # leading spaces
				continue
			elif (s[-i - 1] == ' ' and count > 0): 
				return count
			else:
				count += 1
		return count

if __name__ == "__main__":
	print(Solution.lengthOfLastWord(Solution, "luffy is still joyboy"))
	print(Solution.lengthOfLastWord(Solution, "   fly me   to   the moon  "))
	print(Solution.lengthOfLastWord(Solution, "a"))
