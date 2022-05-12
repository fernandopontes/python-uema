import copy
from lista import Lista

# Ex. 02:
# Escreva uma TAD de lista de inteiros ordenada simplesmente encadeada
# com as seguintes operações:
# a) Verificar se um número pertence lista;
# b) Inserir um novo elemento na lista mantendo a ordem;
# c) Remover um elemento da lista;
# d) Imprimir os valores da lista;
# e) Copiar uma lista l1 para uma lista l2;
# f) Concatenar uma lista l1 com uma lista l2;
# g) Intercalar l1 e l2;
# Exercícios extra que não se aplicam a Lista Ordenada, devem ser aplicados na super classe
# h) Inserir um elemento no início da lista;
# i) Inserir um elemento no meio da lista;
# j) Remover um elemento da Lista;

class ListaEx02(Lista):

    def __init__(self, lst=None):
        super().__init__(lst)

    def msg_check_list(self, number):
        if self.check_in_list(number):
            print(f'O número {number} está na lista!')
        else:
            print(f'O número {number} não está na lista!')

    def check_in_list(self, number):
        if number in self.items:
            return True
        else:
            return False

    def insert_number_list(self, number):
        if(self.check_in_list(number)):
            self.msg_check_list(number)
        else:
            self.insert_eol(number)
            self.items = self.quicksort(self.items)
            print(f'O número {number} foi inserido e ordenado na lista!')
            

    def remove_number_list(self, number):
        if(self.check_in_list(number)):
            index = self.items.index(number)
            del self.items[index]
            print(f'O número {number} foi removido da lista!')
        else:
            self.msg_check_list(number)

    def copy_list(self):
        list = self
        list_copy = copy.deepcopy(list)
        list_copy.print_list()

    def concat_lists(self, listTwo):
        self.items = self.items + listTwo

    def interleave_lists(self, listTwo):
        self.items = [val for pair in zip(self.items, listTwo) for val in pair]

    # Author: https://github.com/laurentluce/
    def quicksort(self, lst):
        if len(lst) <= 1:
            return lst

        pivot = lst[0]
        less = []
        equal = []
        greater = []
        for e in lst:
            if e < pivot:
                less.append(e)
            elif e == pivot:
                equal.append(e)
            else:
                greater.append(e)

        return self.quicksort(less) + equal + self.quicksort(greater)

if __name__ == '__main__':
    print('Exercício 02 da Lista de Exercícios 02')

    lista = ListaEx02([1, 2, 3, 4, 5, 8])

    print('\n# Resolução da letra a:')
    result = lista.msg_check_list(12)

    print('\n# Resolução da letra b:')
    lista.insert_number_list(7)

    print('\n# Resolução da letra c:')
    lista.remove_number_list(5)

    print('\n# Resolução da letra d:')
    lista.print_list()

    print('\n# Resolução da letra e:')
    lista.copy_list()

    print('\n# Resolução da letra f:')
    lista.concat_lists([20, 21, 22, 23, 24, 25])
    lista.print_list()

    print('\n# Resolução da letra g:')
    lista.interleave_lists([20, 21, 22, 23, 24, 25])
    lista.print_list()