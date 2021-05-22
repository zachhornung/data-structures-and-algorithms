class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, search_value):
        current = self.head
        while current:
            if current.value == search_value:
                return True
            current = current.next
        return False

    def __str__(self):
        string = ''
        current = self.head
        while current:
            string += f'{current.value} --> '
            current = current.next
        string += 'None'
        return string

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next