class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		NOT_FOUND = -1
		if (len(needle) == 0):
			return 0
		if (len(haystack) < len(needle)):
			return NOT_FOUND
		result = NOT_FOUND
		for i in range(len(haystack) - len(needle) + 1):
			if (haystack[i:i+len(needle)] == needle[0:len(needle)]):
				result = i
			if (result != NOT_FOUND):
				break
			else:
				continue
		return result

if __name__ == "__main__":
	print(Solution.strStr(Solution, "hay hay hay hay needle hay hay", "needle"))
	print(Solution.strStr(Solution, "needle hay hay hay needle hay hay", "needle"))
	print(Solution.strStr(Solution, "hay hay hay hay hay hay hay", "needle"))
	print(Solution.strStr(Solution, "12312423543364893781462716418724621874", "1462"))




