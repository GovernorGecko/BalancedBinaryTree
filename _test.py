"""
tests related to Balanced Binary Tree
"""

# from src.binarynode import BinaryNode
from PIL import Image, ImageDraw
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

im = Image.new(mode="RGB", size=(200, 200))
draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
 
# This method will show image in any image viewer
# im.show()



