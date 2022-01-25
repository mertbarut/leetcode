from typing import Optional

# Definition for singly-linked list.
class ListNode:
	# constructor
	def __init__(self, val = 0, next = None):
		self.val = val
		self.next = next

class Solution:
	def sortedInsert(self, head: ListNode, newnode: ListNode) -> ListNode:
		current = None
		if (not head or head.val >= newnode.val):
			newnode.next = head
			head = newnode
		else:
			current = head
			while (current.next and current.next.val < newnode.val):
				current = current.next
			newnode.next = current.next
			current.next = newnode
		return head

	def insertionSort(self, head: Optional[ListNode]) -> Optional[ListNode]:		
		sorted = None
		current = head
		while (current):
			next = current.next
			sorted = Solution.sortedInsert(Solution, sorted, current)
			current = next
		head = sorted
		return head

	def sortedInsert(self, head: ListNode, newnode: ListNode) -> ListNode:
		current = None
		if (not head or head.val >= newnode.val):
			newnode.next = head
			head = newnode
		else:
			current = head
			while (current.next and current.next.val < newnode.val):
				current = current.next
			newnode.next = current.next
			current.next = newnode
		return head

	def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
		if (list1):
			current = list1
			while (current.next):
				current = current.next
			if (list2):
				current.next = list2
			return Solution.insertionSort(Solution, list1)
		else:
			return Solution.insertionSort(Solution, list2)

if __name__ == "__main__":
	node1 = ListNode(13)
	node2 = ListNode(177)
	node3 = ListNode(23)

	node1.next = node2
	node2.next = node3

	node4 = ListNode(462)
	node5 = ListNode(646)
	node6 = ListNode(128)

	node4.next = node5
	node5.next = node6

	node1 = Solution.mergeTwoLists(Solution, node1, node4)
	print(node3.next.val)
