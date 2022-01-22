class Solution:
	def getInteger(self, s: str) -> int:
		if (s == 'I'): return 1
		if (s == 'V'): return 5
		if (s == 'X'): return 10
		if (s == 'L'): return 50
		if (s == 'C'): return 100
		if (s == 'D'): return 500
		if (s == 'M'): return 1000

	def romanToInt(self, s: str) -> int:
		n = len(s)
		result = 0
		i = 0
		while (i < n):
			if (i == n - 1): # length == 1
				result = result + Solution.getInteger(Solution, s[i])
				return result
			current = Solution.getInteger(Solution, s[i])
			next = Solution.getInteger(Solution, s[i + 1])
			if (current >= next):
				result += current
				i += 1
			else:
				result += next - current
				i += 2
		return result

if __name__ == '__main__':
	print(Solution.romanToInt(Solution , "I"))
	print(Solution.romanToInt(Solution , "IV"))
	print(Solution.romanToInt(Solution , "XIII"))
	print(Solution.romanToInt(Solution , "XLII"))
	print(Solution.romanToInt(Solution , "LXVII"))
	print(Solution.romanToInt(Solution , "DCLXXX"))
	print(Solution.romanToInt(Solution , "CMXCIX"))
	print(Solution.romanToInt(Solution , "MMMCDXC"))
	print(Solution.romanToInt(Solution , "DXII"))
	print(Solution.romanToInt(Solution , "MMMMCMXCIX"))