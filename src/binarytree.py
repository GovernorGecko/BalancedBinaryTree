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

    def get_height(self):
        """
        """
        if self.__root is not None:
            return self.__root.get_height()
        return 0

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
        left_node_height, right_node_height = self.get_height()

        # Can't be more than 1 difference
        if abs(left_node_height - right_node_height) > 1:
            print("YEAP")
