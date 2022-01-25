from typing import List

class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		N = len(nums)
		if (N < 1):
			return 0
		k = 0
		for i in range(1, N):
			if nums[i] == nums[i - 1]:
				pass
			else:
				k += 1
				nums[k] = nums[i]
		nums = nums[0:(k + 1)]
		return len(nums)

if __name__ == "__main__":
	print(Solution.removeDuplicates(Solution, [0, 0, 1, 1, 2, 3]))
	print(Solution.removeDuplicates(Solution, [0, 1, 1, 2, 2, 3]))
	print(Solution.removeDuplicates(Solution, [0, 2, 4, 4, 5, 5]))
	print(Solution.removeDuplicates(Solution, [0, 1, 2, 3, 4, 5]))
