from typing import List

class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		length = len(nums)
		i = 0
		while (i < length):
			if (nums[i] == val):
				nums.pop(i)
				length -= 1
			else:
				i += 1
		#print(nums)
		return length

if __name__ == "__main__":
	print(Solution.removeElement(Solution, [0, 0, 1, 2, 5, 8, 9, 22, 35, 64, 78], 22))
	print(Solution.removeElement(Solution, [0, 0, 1, 21, 52, 834, 92242, 22232, 351, 643, 781], 834))
	print(Solution.removeElement(Solution, [0, 0, 1, 1, 2, 2, 2, 22232, 324, 5, 5], 2))
	print(Solution.removeElement(Solution, [0, 1, 2, 2, 3, 0, 4, 2], 2))





