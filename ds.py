class Stack:
	def __init__(self):
		self.stack = list()
	def push(self,item):
		self.stack.append(item)
	def pop(self):
		if len(self.stack)>0:
			return self.stack.pop()
		else:
			return None
	def peek(self):
		if len(self.stack)>0:
			return self.stack[len(self.stack)-1]
		else:
			return None
	def __str__(self):
		return str(self.stack)

class Queue:
	def __init__(self):
		self.queue = list()
		self.size = 0
	def enqueue(self,item):
		self.queue.append(item)
		self.size += 1

	def dequeue(self):
		if len(self.queue)>0:
			item = self.queue[0]
			self.queue.remove(item)
			return item
		else:
			return None

	def get_size(self):
		if len(self.queue)>0:
			return self.size
		else:
			return None
	def __str__(self):
		return str(self.queue)

class MaxHeap:
	def __init__(self,items=[]):
		super().__init__()
		self.heap=[0]
		for item in items:
			self.heap.append(item)
			self.__floatUp(len(self.heap)-1)

	def push(self,item):
		self.heap.append(item)
		self.__floatUp(len(self.heap)-1)

	def peek(self):
		if self.heap[1]:
			return self.heap[1]
		else:
			return False

	def pop(self):
		if len(self.heap)>2:
			self.__swap(1,len(self.heap)-1)
			max = self.heap.pop()
			self.__bubbleDown(1)
		elif len(self.heap)==2:
			max=self.heap.pop()
		else:
			max = False
		return max

	def __swap(self,i,j):
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

	def __floatUp(self, index):
		parent = index // 2
		if index <=1:
			return
		if self.heap[parent] < self.heap[index]:
			self.__swap(index,parent)
			self.__floatUp(parent)

	def __bubbleDown(self,index):
		left = index * 2
		right = index *2 +1
		largest = index
		if len(self.heap) > left and self.heap[largest] < self.heap[left]:
			largest = left
		if len(self.heap) > right and self.heap[largest] < self.heap[right]:
			largest = right
		if largest != index:
			self.__swap(largest,index)
			self.__bubbleDown(largest)

	def __str__(self):
		return str(self.heap)



