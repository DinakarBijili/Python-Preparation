class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    # def to_list(self):
    #     l = []
    #     if self.head is None:
    #         return l

    #     node = self.head
    #     while node:
    #         l.append(node.data)
    #         node = node.next_node
    #     return l

    def print_ll(self):
        ll_string = ""
        node = self.head

        while node != None:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node

        ll_string += "tail"
        print(ll_string)

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    


if __name__ == "__main__":
    l = LinkedList()
    l.insert_beginning(1)
    l.insert_beginning("data")
    l.insert_beginning(1)
    l.insert_beginning(1)
    l.insert_at_end(3)
    l.insert_at_end(3)
    l.insert_at_end("data 2")
   
    # result = l.remove(1)
    l.print_ll()