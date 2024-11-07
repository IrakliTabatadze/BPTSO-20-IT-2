class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def remove_at(self, index):
        if index < 0 or self.head is None:
            return

        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        current_position = 0

        while current_node.next and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        if current_node.next:
            current_node.next = current_node.next.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next

        print()


linked_list = LinkedList()

linked_list.append(50)  # 0
linked_list.append(15)  # 1
linked_list.append(20)  # 2
linked_list.append(11)  # 3
linked_list.append(5)  # 4
linked_list.append(25)  # 5

linked_list.display()
linked_list.remove_at(2)
linked_list.display()
linked_list.remove_at(2)
linked_list.display()
linked_list.remove_at(0)
linked_list.display()
linked_list.remove_at(2)
linked_list.display()
