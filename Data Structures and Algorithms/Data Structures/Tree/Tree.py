# """
# The root of the tree is the node with no parents. There can be at most one root node in a tree.
# The edge refers to the link from parent to child.
# A node with NO children is called leaf node.
# Children of same parent are called siblings.


# """
# class Node(object):
#     def __init__(self, data = None):
#         self.left = None
#         self.right = None
#         self.data = data
    
#     # for setting left node
#     def setLeft(self, node):
#         self.left = node
    
#     # for setting right node
#     def setRight(self, node):
#         self.right = node
        
#     # for getting the left node
#     def getLeft(self):
#         return self.left
    
#     # for getting right node
#     def getRight(self):
#         return self.right
    
#     # for setting data of a node
#     def setData(self, data):
#         self.data = data
        
#     # for getting data of a node
#     def getData(self):
#         return self.data
    
# root = Node(1)
# root.setLeft(Node(2))
# root.setRight(Node(3))
# root.left.setLeft(Node(4))

# ''' This will a create like this 
#                     1
#                 /       \
#             2            3
#         /
#     4
# '''


# #Tree Travesal
# # Inorder (left, data, right)
# # Preorder (data, left, right)
# # Postorder (left, right, data)

# # Implementing tree traversals

# # in this we traverse first to the leftmost node, then print its data and then traverse for rightmost node
# def inorder(Tree):
#     if Tree:
#         inorder(Tree.getLeft())
#         print(Tree.getData(), end = ' ')
#         inorder(Tree.getRight())
#     return

# # in this we first print the root node and then traverse towards leftmost node and then to the rightmost node
# def preorder(Tree):
#     if Tree:
#         print(Tree.getData(), end = ' ')
#         preorder(Tree.getLeft())
#         preorder(Tree.getRight())
#     return 

# # in this we first traverse to the leftmost node and then to the rightmost node and then print the data
# def postorder(Tree):
#     if Tree:
#         postorder(Tree.getLeft())
#         postorder(Tree.getRight())
#         print(Tree.getData(), end = ' ')
#     return

# print('Inorder  Traversal:')
# inorder(root)
# print('\nPreorder Traversal:')
# preorder(root)
# print('\nPostorder Traversal:')
# postorder(root)

#OUTPUT:-
# Inorder  Traversal:
# 4 2 1 3 
# Preorder Traversal:
# 1 2 4 3 
# Postorder Traversal:
# 4 2 3 1 

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    

class BinarySearchTree:
    def __init__(self) :
        self.root = None #Top node of Tree

    
    def _insert_recursive(self, value, node): #here node -> Top node and value-> that we insert 
        #Left side
        if value < node.data: # if our given value is lesstha data goes to left
            if node.left is None:
                node.left = TreeNode(value) #if left node is None
            else:
                self._insert_recursive(value, node.left) # from left if not None node becomes node.left
        #Right side
        elif value > node.data:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(value, node.right)

        else:
            return None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value) #TOP VALUE
        else:
            self._insert_recursive(value, self.root)
if __name__ == "__main__":
    Tree = BinarySearchTree()
    Tree.insert(20)
    Tree.insert(1)
    Tree.insert(2)
    Tree.insert(30)
    
        
        
