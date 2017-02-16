class Stack():
	def __init__(self, maxSize):
		self.data = [None] * maxSize 
		self.top = 0  # top index of stack

	def push(self, item):
		if self.top == len(self.data):
			# return str('do not push. stack is full')
			raise str('do not push. stack is full')
		else:
			self.data[self.top] = item
			self.top += 1

	def pop(self):
		if self.data[self.top-1] is None:
			raise str('stack is empty')
		else:
			result = self.data[self.top-1]
			self.data[self.top-1] = None
			self.top -= 1
			return result

	def __iter__(self):
		i = 0
		while i < self.top:
			yield self.data[i]
			i += 1

	def __str__(self):
		if self.top == 0:
			return str(None)
		else:
			values = [str(x) for x in self]
			return ' | '.join(values)


if __name__ == '__main__':
	st = Stack(10)
	st.push(1)
	st.push(2)
	st.push(3)
	st.push(4)
	st.push(5)
	st.push(6)
	st.push(7)
	st.push(8)
	st.push(9)
	st.push(10)
	# st.push(11)
	print(st)
	print(st.top)
	st.pop()
	st.pop()
	st.pop()
	st.pop()
	st.pop()
	st.pop()
	st.pop()
	st.pop()
	st.pop()
	st.pop()

	st.pop() # error 

	print(st)
	print(st.top)