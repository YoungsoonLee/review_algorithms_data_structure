""" 
	FIFO
	enqueue, dequeue
	use list function
"""
class Queue():
	def __init__(self, maxSize):
		self.data = [None] * maxSize
		self.count = 0
	
	def __iter__(self):
		i = 0
		while i < self.count:
			yield self.data[i]
			i += 1

	def __str__(self):
		if self.count == 0:
			return str(None)
		else:
			values = [str(x) for x in self]
			return ' | '.join(values)

	def enqueue(self, item):
		if self.count == len(self.data):
			return str('queue is full')
		else:
			self.data[self.count] = item
			self.count += 1

	def dequeue(self):
		if self.count == 0:
			return str('queue is empty')
		else:
			result = self.data[0]
			del self.data[0]
			self.count -= 1			
			return result

if __name__ == '__main__':
	q = Queue(10)
	q.enqueue(1)
	q.enqueue(2)
	print(q)
	q.dequeue()
	print(q)
	#pint(q.count)
	print(q.count)

