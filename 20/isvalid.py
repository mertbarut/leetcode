class Solution:
	def isValid(self, s: str) -> bool:
		open_list = ["[","{","("]
		close_list = ["]","}",")"]
		stack = []
		for i in s:
			if i in open_list:
				stack.append(i)
			elif i in close_list:
				pos = close_list.index(i)
				if (stack and (open_list[pos] == stack[-1])):
					stack.pop()
				else:
					return False
		if not stack:
			return True
		else:
			return False

if __name__ == "__main__":
	print(Solution.isValid(Solution, "()[]{}"))
	print(Solution.isValid(Solution, "(){}"))
	print(Solution.isValid(Solution, "[]{}"))
	print(Solution.isValid(Solution, "()[]"))
	print(Solution.isValid(Solution, "(TEST)"))
	print(Solution.isValid(Solution, "(TEST)[TEST]{TEST}]"))
	print(Solution.isValid(Solution, "([)]"))
	print(Solution.isValid(Solution, "{[]}"))
	print(Solution.isValid(Solution, "(])"))
	

