class Node:
	def __init__(self, item=None):
		self.data = item
		self.next = None

	def __str__(self):
		return str(self.data)

class LinkedList:
	def __init__(self):
		self.length = 0
		self.head = None

	def add(self, item):
		node = Node(item)
		current = self.head
		if current is None:
			self.head = node
		else:
			while current.next:
				current = current.next
			current.next = node
		self.length += 1

	# get item at the position
	def search(self, position):
		current = self.head
		index = 0
		if position >= self.length:
			return None
		else:
			while index < position:
				current = current.next
				index += 1
		return current.data

	# remove item 
	def remove(self, item):
		current = self.head
		if current.data == item:  # found at the first
			self.head = current.next
		else:
			while current.data != item:
				prev = current
				current = current.next
			prev.next = current.next
		self.length -= 1

	def __iter__(self):
		current = self.head
		while current:
			yield current
			current = current.next
	
	def __str__(self):
		values = [str(data) for data in self]
		return ' -> '.join(values)

	

if __name__ == "__main__":
	# node = Node()
	linkedlist = LinkedList()
	# linkedlist.head = node
	linkedlist.add(1)
	linkedlist.add(2)
	linkedlist.add(3)
	print(linkedlist)
	# print(linkedlist.head)
	# print(linkedlist.head.data)
	# print(linkedlist.head.next.data)
	# print(linkedlist.length)
	# print(linkedlist.search(1))
	linkedlist.remove(2)
	print(linkedlist)
