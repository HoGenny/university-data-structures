class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def insert(where, data):
    global head
    newNode = Node('자료')
    pre = head
    for _ in range(where - 1):
        pre = pre.next
    newNode.next = pre.next
    pre.next = newNode

def delete(data):
    global head
    pre = head
    while pre.next.data != data:
        pre = pre.next
    pre.next = pre.next.next

def print_list():
    global head
    p = head
    while p:
        print(p.data)
        p = p.next

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
node5 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

head = node1
insert(3, '자료')
print_list()
delete('자료')
print_list()