import sys

N = int(sys.stdin.readline().rstrip())
tree = {}

for i in range(N):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left, right]


def preorder(r):
    if r != '.':
        print(r, end='')
        preorder(tree[r][0])
        preorder(tree[r][1])

    return


def inorder(r):
    if r != '.':
        inorder(tree[r][0])
        print(r, end='')
        inorder(tree[r][1])

    return


def postorder(r):
    if r != '.':
        postorder(tree[r][0])
        postorder(tree[r][1])
        print(r, end='')

    return


preorder('A')
print("")
inorder('A')
print("")
postorder('A')
