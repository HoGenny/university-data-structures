import sys
sys.stdin = open('input.txt', 'r')

V, E = map(int, input().split())
tree = [[0] * 5 for _ in range(V + 1)]
data = list(map(int, input().split()))

for i in range(V):
    tree[i][3] = tree[i][4] = -1

tree[1][4] = 0

def preorder(T):
    if T:
        print("%d" %T, end = ' ')
        preorder(tree[T][0])
        preorder(tree[T][1])

def inorder(T):
    if T:
        inorder(tree[T][0])
        print("%d" %T, end = ' ')
        inorder(tree[T][1])

def postorder(T):
    if T:
        postorder(tree[T][0])
        postorder(tree[T][1])
        print("%d" %T, end = ' ')

for i in range(E):
    parent, child = data[i*2:i*2+2]
    if tree[parent][0] == 0:
        tree[parent][0] = child
        tree[parent][2] += 1
        tree[child][3] = parent
        tree[child][4] = tree[parent][4] + 1
    else:
        tree[parent][1] = child
        tree[parent][2] += 1
        tree[child][3] = parent
        tree[child][4] = tree[parent][4] + 1

preorder(1)
print()
inorder(1)
print()
postorder(1)