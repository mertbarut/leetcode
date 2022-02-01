from typing import List

class Solution:
	def	recursive(self, i, digits: List[int], sz):
		if digits[-i] == 9 and i <= sz :
			digits[-i] = 0
			if i == sz:
				digits.insert(0, 1)
				return digits
			Solution.recursive(self, i + 1, digits, sz)
		else:
			digits[-i] += 1
		return digits

	def plusOne(self, digits: List[int]) -> List[int]:
		return Solution.recursive(self, 1, digits, len(digits))

if __name__ == "__main__":
	print(Solution.plusOne(Solution, [1,4,3]))
	print(Solution.plusOne(Solution, [9,9]))
	print(Solution.plusOne(Solution, [9]))