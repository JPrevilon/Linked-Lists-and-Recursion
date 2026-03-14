class Node:
    """
    A Node class to store integer data and a reference to the next node.
    """

    def __init__(self, data):
        # Store the node data
        self.data = data

        # Pointer to next node
        self.next = None


class LinkedList:
    """
    A singly linked list that holds Node objects and performs operations using recursion.
    """

    def __init__(self):
        # Head pointer starts as None (empty list)
        self.head = None

    def insert_at_front(self, data):
        """
        Insert a new node at the front of the list.
        """

        new_node = Node(data)

        # New node points to current head
        new_node.next = self.head

        # Update head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert node at the end of the list.
        """

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        """
        Recursively sum all node values in the list.
        """

        def helper(node):
            if node is None:
                return 0

            return node.data + helper(node.next)

        return helper(self.head)

    def recursive_reverse(self):
        """
        Reverse the linked list using recursion.
        """

        def helper(prev, current):

            if current is None:
                return prev

            next_node = current.next
            current.next = prev

            return helper(current, next_node)

        self.head = helper(None, self.head)

    def recursive_search(self, target):
        """
        Recursively search for a value in the list.
        """

        def helper(node):

            if node is None:
                return False

            if node.data == target:
                return True

            return helper(node.next)

        return helper(self.head)

    def display(self):
        """
        Print the linked list contents.
        """

        current = self.head
        values = []

        while current:
            values.append(str(current.data))
            current = current.next

        values.append("None")

        print(" -> ".join(values))