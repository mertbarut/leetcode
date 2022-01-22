from typing import List

class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		if not strs: return ""
		s1 = min(strs)
		s2 = max(strs)
		for i, c in enumerate(s1):
			if c != s2[i]:
				return s1[:i]
		return s1

if __name__ == "__main__":
	print(Solution.longestCommonPrefix(Solution, ["flower", "flex", "flare"]))
	print(Solution.longestCommonPrefix(Solution, ["no", "common", "prefix"]))
	