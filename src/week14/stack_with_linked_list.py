class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
    def pop(self):
        data = None
        if self.top is None:
            print("스택이 비었습니다.")
        else:
            data = self.top.data
            self.top = self.top.next
            return data
    def whatisTop(self):
        data = None
        if self.top is None:
            print("스택이 비었습니다.")
        else:
            data = self.top.data
        return data

a = Stack()
a.push(10)
a.push(20)
a.push(30)
print(a.whatisTop())
print(a.pop())
print(a.pop())
print(a.pop())