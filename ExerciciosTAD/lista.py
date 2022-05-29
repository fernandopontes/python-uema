class Lista:
    def __init__(self, lst=None):
        self.items = []
        if lst is not None:
            self.items = lst

    def is_empty(self):
        return self.items == []

    def insert_bol(self, item):
        self.items.insert(0, item)

    def insert_mol(self, item):
        mposition = len(self.items)//2
        self.items = self.items[0:mposition] + [item] + self.items[mposition:]

    def insert_eol(self, item):
        self.items.append(item)

    def remove_bol(self):
        first = self.items[0]
        del self.items[0]
        return first

    def remove_mol(self):
        index = len(self.items) % 2
        if index == 0:
            print('A sua lista tem uma quantidade par no total de elementos')
            mposition = len(self.items)//2
            mpostionLeft = mposition - 1
            numberLeft = self.items[mpostionLeft]
            mpositionRight = mposition
            numberRight = self.items[mpositionRight]
            number = int(input(f"Qual número [{self.items[mpostionLeft]}, {self.items[mpositionRight]}] você deseja excluir? "))
            if number == numberLeft: 
                del self.items[mpostionLeft]
            elif number == numberRight:   
                del self.items[mpositionRight]
            else:
                print(f"O número digitado não corresponde às opções [{self.items[mpostionLeft]}, {self.items[mpositionRight]}]")
            return 
        else:
            mposition = len(self.items)//2
            del self.items[mposition]

    def remove_eol(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_list(self):
        for item in self.items:
            print(item)

class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    # similar to_string()
    def __repr__(self):
        node = self.head
        nodes  = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    # similar to for()
    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        for node in self:
            if node.data == target_node_data:
                new_node.next = node.next
                node.next = new_node
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        
        raise Exception("Node with data '%s' not found" % target_node_data)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data