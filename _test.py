"""
tests related to Balanced Binary Tree
"""

# from src.binarynode import BinaryNode
from src.binarytree import BinaryTree

# bn = BinaryNode(1)
# bn.insert_node(BinaryNode(2))
# print(bn)

bt = BinaryTree()
bt.insert_value(4)
bt.insert_value(1)
bt.insert_value(3)
bt.insert_value(2)
bt.insert_value(10)
print(bt)
print(bt.get_height())
