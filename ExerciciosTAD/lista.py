from collections import deque

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


list = Lista([1, 2, 3, 4, 5, 6, 7, 8])
list.print_list()
print("\n")
list.remove_mol()
list.print_list()
# list.insert_bol('5')
# list.print_list()
# print("\n")
# list.remove_bol()
# list.print_list()
# print("\n")
# list.remove_mol()
# list.print_list()
# list.insert_mol('2.5');
# list.print_list()
