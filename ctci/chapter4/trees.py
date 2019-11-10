class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# To create a BST
def insertIntoBST(root, number):
    if root is None:
        return Node(number)

    if root.data < number:
        root.right = insertIntoBST(root.right, number)
    elif root.data >= number:
        root.left = insertIntoBST(root.left, number)

    return root

# Inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def isBST(root):
    return isBSTUtil(root, float('-inf'), float('inf'))

def isBSTUtil(root, min, max):
    if root is None:
        return True
    
    if root.data <= min or root.data > max:
        return False

    if not isBSTUtil(root.left, min, root.data) or not isBSTUtil(root.right, root.data, max):
        return False
    
    return True

def getHeight(root=None):
    if root is None:
        return 0

    return 1 + max(getHeight(root.left), getHeight(root.right))

def isBalanced(root=None):
    if root:
        return isBalanced(root.left) and isBalanced(root.right) and abs(getHeight(root.left) - getHeight(root.right)) <= 1
    return True    

if __name__ == "__main__":
    inputList = [28, 15, 9, 5, 4, 1, 6, 31, 45, 79, 33, 42]
    root1 = Node(inputList.pop(0))

    for number in inputList:
        root1 = insertIntoBST(root1, number)
    
    print(isBST(root1))
    print(getHeight(root1))
    print(isBalanced(root1))