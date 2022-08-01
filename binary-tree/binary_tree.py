# https://github.com/laurentluce/python-algorithms/blob/master/algorithms/binary_tree.py
class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def lookup(self, data, parent=None):
        if data < self.data:
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)
        elif data > self.data:
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else:
            return self, parent


    def delete(self, data):
        # get node containing data
        node, parent = self.lookup(data)
        if node is not None:
            children_count = node.children_count()
            if children_count == 0:
                if parent:
                    if parent.left is node:
                        parent.left = None
                    else:
                        parent.right = None
                else:
                    self.data = None
            elif children_count == 1:
                if node.left:
                    n = node.left
                else:
                    n = node.right
                if parent:
                    if parent.left is node:
                        parent.left = n
                    else:
                        parent.right = n
                else:
                    self.left = n.left
                    self.right = n.right
                    self.data = n.data
            else:
                parent = node
                successor = node.right
                while successor.left:
                    parent = successor
                    successor = successor.left
                # replace node data by its successor data
                node.data = successor.data
                # fix successor's parent node child
                if parent.left == successor:
                    parent.left = successor.right
                else:
                    parent.right = successor.right


    def children_count(self):
        cnt = 0
        if self.left:
            cnt += 1
        if self.right:
            cnt += 1
        return cnt


    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=" ")
        if self.right:
            self.right.print_tree()


if __name__ == '__main__':
    print('Exercício de Árvores Binárias de Pesquisa (ABP)')

    print('\n')
    print('#### ABP 1 ####')
    print('\n')

    tree = Node(60)
    tree.insert(59)
    tree.insert(55)
    tree.insert(50)
    tree.insert(40)
    tree.insert(65)
    tree.insert(70)
    tree.insert(80)
    tree.insert(75)
    tree.insert(90)
    print('\n')
    tree.print_tree()
    tree.delete(80)
    print('\n')
    tree.print_tree()

    list = [70, 75, 80, 6, 10, 20]

    i=1
    for number in list:
        if(i == 1):
            tree2 = Node(number)
        else:
            tree2.insert(number)
        i += 1

    print('\n')
    print('#### ABP 2 ####')
    print('\n')
    tree2.print_tree()
        
