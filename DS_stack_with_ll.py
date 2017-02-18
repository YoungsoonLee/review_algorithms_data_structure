class Node():
	def __init__(self, item=None):
		self.data = item
		self.next = None

	def __str__(self):
		return str(self.data)


class Stack():
	def __init__(self):
		self.top = None
		self.count = 0

	def push(self, item):
		node = Node(item)
		cur = self.top
		if cur is None:
			self.top = node
		else:
			while cur.next:
				cur = cur.next			
			cur.next = node
		self.count += 1

	def pop(self):
		cur = self.top
		pre = None
		while cur.next:
			pre = cur
			cur = cur.next
		value = cur
		pre.next = None
		return value

	def getTopIndex(self):
		cur = self.top
		index = 0
		while cur:
			cur = cur.next
			index += 1
		return index-1

	def __iter__(self):
		cur = self.top
		# print(cur)
		while cur:
			yield cur.data
			cur = cur.next

	def __str__(self):
		values = [str(x) for x in self]
		# print(values)
		return ' | '.join(values)


if __name__ == "__main__":
	st = Stack()
	st.push(1)
	st.push(2)
	st.push(3)
	st.push(4)
	st.push(5)
	st.push(6)
	st.push(7)
	print(st)
	print(st.getTopIndex())
	print(st.pop())
	print(st.pop())
	print(st.pop())
	print(st)
	