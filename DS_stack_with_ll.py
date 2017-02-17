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
			self.top = cur
		self.count += 1

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

