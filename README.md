# Implementation for the Data Structures 

from lot import Stack
from lot import Queue
from lot import MaxHeap

mystack=Stack()
mystack.push(1)
mystack.push(2)
print(mystack.peek())
print(mystack.pop())
print(mystack)

myqueue=Queue()
myqueue.enqueue(15)
myqueue.enqueue(10)
myqueue.enqueue(17)
print(myqueue.get_size())
print(myqueue.dequeue())
print(myqueue)

my=MaxHeap([95,3,21])
my.push(15)
my.push(14)
my.push(20)
my.push(18)
print(my)
print(my.peek())
print(my.pop())
print(my.peek())
print(my.pop())
print(my.peek())
print(my.pop())
