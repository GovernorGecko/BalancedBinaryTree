"""
binarynode.py
"""


class BinaryNode():
    """
    """

    __slots__ = [
        "__left_node", "__parent_node", "__right_node", "__value"
    ]

    def __init__(self, value, parent_node=None):

        if not isinstance(value, (int, float)):
            raise ValueError("Value must be of type int or float.")

        # Set Values
        self.__left_node = None
        self.__parent_node = parent_node
        self.__right_node = None
        self.__value = value

    def __str__(self):
        """
        returns
            string
        """
        return f"{self.__left_node} {self.__value} {self.__right_node}"

    def get_height(self):
        """
        """

        # Fetch the left node height
        left_node_height = 1
        if self.__left_node is not None:
            left_node_height += max(self.__left_node.get_height())

        # Fetch the right node height
        right_node_height = 1
        if self.__right_node is not None:
            right_node_height += max(self.__right_node.get_height())

        # Return a tuple
        return (left_node_height, right_node_height)

    def get_value(self):
        """
        returns
            int/float
        """
        return self.__value

    def insert_node(self, node):
        """
        """

        if type(node).__name__ != "BinaryNode":
            raise ValueError("Node must be a BinaryNode.")

        # Less than us?
        if node.get_value() < self.__value:

            # If we have a left node, pass along
            if self.__left_node is not None:
                self.__left_node.insert_node(node)
            # We don't, so set it
            else:
                self.__left_node = node

        # Greater than us?
        elif node.get_value() > self.__value:

            # IF we have a right node, pass along
            if self.__right_node is not None:
                self.__right_node.insert_node(node)

            # We don't, so set it
            else:
                self.__right_node = node

        # Value is equal to us, not implemented
        else:
            print("Same value as us, need to implement that...")
