
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, data):
        if root is None:
            return Node(data)

        if data < root.data:
            root.left = self.insert(root.left, data)
        elif data > root.data:
            root.right = self.insert(root.right, data)

        return root

    def search(self, root, key):
        if root is None or root.data == key:
            return root

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            temp = root.right
            while temp.left:
                temp = temp.left

            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


# Main Program
bt = BST()

values = [50, 30, 70, 20, 40, 60, 80]

for i in values:
    bt.root = bt.insert(bt.root, i)

print("BST Elements:")
bt.inorder(bt.root)

key = 40
print("\nSearch:", "Found" if bt.search(bt.root, key) else "Not Found")

bt.root = bt.delete(bt.root, 30)

print("After Deletion:")
bt.inorder(bt.root)
