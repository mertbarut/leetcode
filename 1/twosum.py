from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		hashmap = {}
		for i in range(len(nums)):
			hashmap[nums[i]] = i
			#print(hashmap[nums[i]], ":", nums[i])
		for i in range(len(nums)):
			complement = target - nums[i]
			if complement in hashmap and hashmap[complement] != i:
				return [i, hashmap[complement]]

if __name__ == "__main__":
	print("nums = [2, 7, 11, 15], target = 9:", Solution.twoSum(Solution, [2, 7, 11, 15], 9))
	print("nums = [3, 2, 4], target = 6:", Solution.twoSum(Solution, [3, 2, 4], 6))
	print("nums = [3, 3], target = 6:", Solution.twoSum(Solution, [3, 3], 6))
