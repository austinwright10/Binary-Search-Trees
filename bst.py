'''your bst here'''
from typing import Any

class BST:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

        def __str__(self):
            return f"Value: {self.value}"

    def __init__(self):
        self.root = None
        self._size = 0
    
    def size(self):
        return self._size
    
    def is_empty(self):
        if not self.root:
            return True
        else:
            return False
    
    def height(self):
        return self.height_recursive(self.root)
    
    def height_recursive(self, node):
        if node is None:
            return -1
        else:
            left_height = self.height_recursive(node.left)
            right_height = self.height_recursive(node.right)
            return 1 + max(left_height, right_height)
        
    def add(self, item):
        node = self.Node(item)
        if self.root is None:
            self.root = node
            self._size += 1
        else:
            currentNode = self.root
            while currentNode is not None:
                if node.value < currentNode.value:
                    if currentNode.left is None:
                        currentNode.left = node
                        currentNode = None
                        self._size += 1
                        break
                    else:
                        currentNode = currentNode.left
                else:
                    if currentNode.right is None:
                        currentNode.right = node
                        currentNode = None
                        self._size += 1
                        break
                    else:
                        currentNode = currentNode.right

    def remove(self, item):
        self.root = self.remove_recursive(self.root, item)
        return self.root

    def remove_recursive(self, node, item):
        if node is None:
            return self.root
        if item < node.value:
            node.left = self.remove_recursive(node.left, item)
        elif item > node.value:
            node.right = self.remove_recursive(node.right, item)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = node.left
                while successor.right:
                    successor = successor.right
                node.value = successor.value
                node.left = self.remove_recursive(node.left, successor.value)
        self._size -= 1
        return node
    
    def find(self, item):
        currentNode = self.root
        while currentNode is not None:
            if currentNode.value == item:
                return currentNode.value
            elif item < currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
        raise ValueError("Item was not in the tree")
    
    def inorder(self):
        return self._inOrder_recursive(self.root)

    def _inOrder_recursive(self, node):
        my_list = []
        if node is None:
            return my_list
        else:
            my_list.extend(self._inOrder_recursive(node.left))
            my_list.append(node.value)
            my_list.extend(self._inOrder_recursive(node.right))
        return my_list
    
    def preorder(self):
        return self._preOrder_recursive(self.root)

    def _preOrder_recursive(self, node):
        my_list = []
        if node is None:
            return my_list
        else:
            my_list.append(node.value)
            my_list.extend(self._preOrder_recursive(node.left))
            my_list.extend(self._preOrder_recursive(node.right))
        return my_list
    
    def postorder(self):
        return self._postOrder_recursive(self.root)

    def _postOrder_recursive(self, node):
        my_list = []
        if node is None:
            return my_list
        else:
            my_list.extend(self._postOrder_recursive(node.left))
            my_list.extend(self._postOrder_recursive(node.right))
            my_list.append(node.value)
        return my_list

    # def __str__(self):
    #     return f'BST({self.inOrder(self.root)})'
