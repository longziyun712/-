class Node:
	def __init__(self, data, next=None):
		self.data, self.next = data, next

class LinkList:
	def __init__(self):
		self.head = None
	def initList(self, data):
		self.head = Node(data[0])
		p = self.head
		for i in data[1:]:
			node = Node(i)
			p.next = node
			p = p.next
	def insertCat(self):
                if self.head==None:
                    self.head=Node(6)
                    return
                slow=fast=self.head
                while fast.next and fast.next.next:  #不能是next.next在前
                    slow=slow.next
                    fast=fast.next.next
                nd=Node(6)
                nd.next=slow.next
                slow.next=nd
	def printLk(self):
		p = self.head
		while p:
			print(p.data, end=" ")
			p = p.next
		print()

lst = list(map(int,input().split()))
lkList = LinkList()
lkList.initList(lst)
lkList.insertCat()
lkList.printLk()