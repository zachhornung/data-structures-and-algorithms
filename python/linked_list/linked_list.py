class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        self.head = Node(value, self.head)

    # def traverse(self, func):
    #     current = self.head
    #     while current:
    #         func()
    #     current = current.next

    def includes(self, search_value):
        # look_for_value = lambda value: True if value is search_value
        # self.traverse(look_for_value(search_value))
        # return False
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