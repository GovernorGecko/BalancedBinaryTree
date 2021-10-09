"""
binarytree
"""

from .binarynode import BinaryNode


class BinaryTree():
    """
    """

    __slots__ = ["__root"]

    def __init__(self):
        self.__root = None

    def __str__(self):
        """
        returns
            string
        """
        return str(self.__root)

    def insert_value(self, value):
        """
        """

        # No root? Thus it is this.
        if self.__root is None:
            self.__root = BinaryNode(value)
        # Have a root?  Pass along.
        else:
            self.__root.insert_node(BinaryNode(value))

        # We balanced?
