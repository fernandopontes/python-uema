from lista import Node
from lista import Register
from lista import CircularLinkedList

# Ex. 04:
# 1 - Lista circular ordenada duplamente encadeada
# 2 - Armazena em cada nó uma chave inteira e um nome
# 3 - Buscar um nome dado o valor da chave
# 4 - Inserir um novo elemento na lista mantendo a ordem
# 5 - Remover um elemento da lista
# 6 - Imprimir os valores da lista
# 7 - Copiar uma lista l1 para uma lista l2
# 8 - Concatenar uma lista l1 com uma lista l2
# 9 - Intercalar l1 e l2

class ListaEx04(CircularLinkedList):
    list = []
    def __init__(self, registers):
        self.list = registers.copy()
        super().__init__(registers)

    def search_key(self, key):
        node = self.head
        while node is not None:
            if(node.data.key == key):
                return node
            node = node.next 
            if node.data == self.head.data:
                break

    def search_name(self, name):
        node = self.head
        while node is not None:
            if(node.data.name == name):
                return node
            node = node.next 
            if node.data == self.head.data:
                break

    def print_value(self):
        node = self.head
        while node is not None:
            print(node.data.name)
            node = node.next 
            if node.data == self.head.data:
                break

    def copy_list(self):
        list_temp = []
        node = self.head
        while node is not None:
            list_temp.append(node.data)
            node = node.next 
            if node.data == self.head.data:
                break
        return list_temp

    def concat_lists(self, listTwo):
        return self.list + listTwo
            
        
if __name__ == '__main__':
    print('Exercício 04 da Lista de Exercícios 02')

    list = ListaEx04([Register(1, 'Angra'), Register(2, 'Shaman'), Register(3, 'Helloween')])
    
    print('###### EXIBINDO LISTA...######')
    list.print_value()

    print('\n###### PROCURANDO CHAVE "3" NA LISTA...######')
    value = list.search_key(3)
    if(value) :
        print(value.data.name)
    else:
        print('Nada encontrado!')

    print('\n###### ADICIONANDO "Metallica" NA LISTA...######')
    list.add_item(Node(Register(4, 'Metallica')))
    list.print_value()

    print('\n###### REMOVENDO "Helloween" DA LISTA...######')
    value = list.search_name('Helloween')
    if(value):
        list.remove_node(value.data)
    else:
        print('Nada encontrado!')
    list.print_value()

    print('\n###### COPIANDO LISTA...######')
    list2 = list.copy_list()
    list2 = ListaEx04(list2)
    list2.print_value()

    print('\n###### CONCATENANDO LISTA...######')
    list3 = ListaEx04(list.concat_lists([Register(4, 'Metallica'), Register(5, 'Coldplay'), Register(6, 'Imagine Dragons')]))
    list3.print_value()
    
