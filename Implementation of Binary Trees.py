class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:   
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)


def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)


def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")


if __name__ == "__main__":
    root = None
    n = int(input("Enter number of nodes: "))
    
    print("Enter elements:")
    for i in range(n):
        el = input().strip()   
        root = insert(root, el)

    print("\nInorder Traversal: ")
    inorder(root)
    print("\nPreorder Traversal: ")
    preorder(root)
    print("\nPostorder Traversal: ")
    postorder(root)
