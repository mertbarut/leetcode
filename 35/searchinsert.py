from typing import List

class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		for i, item in enumerate(nums):
			if item < target:
				continue
			elif item >= target:
				return i
		return i + 1

if __name__ == "__main__":
	print(Solution.searchInsert(Solution, [1, 3, 5, 6], 5))
	print(Solution.searchInsert(Solution, [1, 3, 5, 6], 2))
	print(Solution.searchInsert(Solution, [1, 3, 5, 6], 7))
