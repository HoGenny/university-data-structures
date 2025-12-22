class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
head = None
tail = None

def addNode(who):
    global head, tail
    newNode = Node(who)
    if not head:
        head = newNode
        tail = newNode
    else:
        tail.next = newNode
        tail = newNode

def thirdwillDie(pre):
    pre = pre.next
    pre.next = pre.next.next
    return pre.next

for who in range(1, 42):
    addNode(who)
tail.next = head
pre = head
while pre.next.next != pre:
    pre = thirdwillDie(pre)

print(pre.data)
print(pre.next.data)