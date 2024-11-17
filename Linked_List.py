#                           <-- Linked List -->

# Creating Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Creating Linked List class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

#                           <--- Insertion -->
    def insert_at_beg(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert_at_place(self, new_node, place):

        if place == 1:
            self.insert_at_beg(new_node)
            return

        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        i = 2
        prev_node = self.head
        current_node = self.head.next

        while current_node is not None and i < place:
            prev_node = current_node
            current_node = current_node.next
            i += 1

        new_node.next = current_node
        prev_node.next = new_node

        if new_node.next is not None:
            tail = new_node



    # <-- printing list -->
    def print(self):
        if self.head is None:
            print("Empty List")
        else:
            out = ''
            current_node = self.head
            while(True):
                if current_node is None:
                    break
                else:
                    out = out + current_node.data
                    if current_node.next is not None:
                        out += ' --> '
                current_node = current_node.next
            print(out)

ele1 = Node('A')
ele2 = Node('B')
ele3 = Node('D')
ele4 = Node('E')

LL = Linked_List()

LL.insert_at_end(ele3)
LL.insert_at_end(ele4)
LL.insert_at_beg(ele2)
LL.insert_at_beg(ele1)

ele5 = Node('C')
LL.insert_at_place(ele5, 3)

LL.print()