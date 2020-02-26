
class Node:
	"""
	A node in a linked list consist of an item value and the pointer/ reference to the next item
	"""
	def __init__(self, data):
		self.item = data
		self.ref = None


class LinkedList:
	"""
	Will  contain one member start_node that will point to the start or the first node of the linked list
	"""
	def __init__(self):
		self.start_node = None

	def traverse_list(self):
		"""
		this is a function for traversing and returning values of a linked list
		:return:
		"""
		if self.start_node is None:
			print "List has no elements"
			return
		else:
			n = self.start_node
			while n is not None:
				print n.item, ''
				n = n.ref

	def insert_at_start(self, data):
		"""
		inserts an item at the beginning of the node and thus the item becomes the start node
		:param data:
		:return:
		"""
		new_node = Node(data)
		new_node.ref = self.start_node
		self.start_node = new_node

	def insert_at_end(self, data):
		"""
		Inserting an Item at the end of the linked list
		:param data:
		:return:
		"""
		new_node = Node(data)
		if self.start_node is None:
			self.start_node = new_node
			return
		n = self.start_node
		while n.ref is not None:
			n = n.ref
		n.ref = new_node

	def insert_after_item(self, x, data):
		"""
		inserting an item after a given item x
		:param x: value of the node that will point to the inserted data
		:param data:
		:return:
		"""
		n = self.start_node
		print(n.ref)
		while n is not None:
			if n.item == x:
				break
			n = n.ref
		if n is None:
			print "Item not in list"
		else:
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node

	def insert_before_item(self, x, data):
		"""
		inserting an item before a given item
		:param x: the item given for you to insert before it
		:param data:
		:return:
		"""
		if self.start_node is None:
			print "The list has no items"
			return
		if x == self.start_node.item:
			new_node = Node(data)
			new_node.ref = self.start_node
			self.start_node = new_node
			return
		n = self.start_node
		while n.ref is not None:
			if n.ref.item == x:
				break
			n = n.ref
		if n.ref is None:
			print "item not in list"
		else:
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node

	def insert_at_index(self, index, data):
		if index == 1:
			new_node = Node(data)
			new_node.ref = self.start_node.ref
			self.start_node = new_node
		i = 1
		n = self.start_node
		while i < index-1 and n is not None:
			n = n.ref
			i +=1
		if n is None:
			print "Index out of bound"
		else:
			new_node = Node(data)
			new_node.ref = n.ref
			n.ref = new_node

	def get_count(self):
		"""
		counts the number of elements in a linked list
		:return:
		"""
		if self.start_node is None:
			return 0
		n = self.start_node
		count = 0
		while n is not None:
			count = count + 1
			n = n.ref
		return count

	def search_item(self, x):
		"""
		for searching if an item exist in a linked linked list
		:param x: the item to be searched
		:return: boolean
		"""
		if self.start_node is None:
			print "List has no elements"
			return
		n = self.start_node
		while n is not None:
			if n.item == x:
				print "Item found"
				return True
			n = n.ref
		print "Item not found"
		return False

	def make_new_list(self):
		"""
		A function for creating a new linked list
		:return:
		"""
		nums = int(input("How many nodes do you want to create: "))
		if nums == 0:
			return
		for i in range(nums):
			value = int(input("Enter the value for the node: "))
			self.insert_at_end(value)

	def delete_at_start(self):
		"""
		delete an element at the start of the linked list
		:return:
		"""
		if self.start_node is None:
			print "The list has no element to delete"
			return
		self.start_node = self.start_node.ref

	def delete_at_end(self):
		"""
		delete an element at the end of the linked list
		:return:
		"""
		if self.start_node is None:
			print "The list has no element to delete"
			return
		n = self.start_node
		while n.ref.ref is not None:
			n = n.ref
		n.ref = None

	def delete_element_by_value(self, x):
		"""
		delete the element value x if it exist in the linked list
		:param x:
		:return:
		"""
		if self.start_node is None:
			print "The list has no element"
			return
		n = self.start_node
		while n.ref is not None:
			if n.ref.item == x:
				break
			n = n.ref
		if n.ref is None:
			print "Item not in list"
		else:
			n.ref = n.ref.ref

	def reverse_list(self):
		"""
		reverse the linked list
		:return:
		"""
		prev = None
		n = self.start_node
		while n is not None:
			next = n.ref
			n.ref = prev
			prev = n
			n = next
			self.start_node = prev

