"""
数据结构中的stack，使用Python自带的list即可实现,LIFO
list的方法有：
	1、append(object)： Append object to the end of the list. O(1)
	2、count(value)：Return number of occurrences of value. O(n)
	3、insert(index, value)：Insert object before index. O(n)
	4、reverse(): Reverse *IN PLACE*.
	5、clear(): Remove all items from list.
	6、extend(iterable): Extend list by appending elements from the iterable. O(n)
	7、pop(index=-1): Remove and return item at index (default last).
	8、sort(*, key=None, reverse=False)
	9、copy():Return a shallow copy of the list.
	10、index(value, start=0, stop=9223372036854775807):Return first index of value.
	11、remove(value): Remove first occurrence of value.
"""

class Stack(object):
	
	def __init__(self):
		self.__data = list()

	def is_empty(self):
		return len(self.__data) == 0

	def pop(self):
		return self.__data.pop()

	def push(self, element):
		self.__data.append(element)

	def get_size(self):
		return len(self.__data)


if __name__ == '__main__':
	stack = Stack()
	for i in range(10):
		stack.push(i)
	while not stack.is_empty():
		print(stack.pop())

