import copy
from tkinter.messagebox import NO

from lista import Node
from lista import LinkedList

# Ex. 03:
# Considere uma coleção de nomes de sites da web e seus respectivos links
# na Internet armazenados através de uma lista simplesmente encadeada.
# Escreva a respectiva estrutura e um método que, dado o nome de um site,
# busque o seu link correspondente na lista e ao mesmo tempo mova o nó que
# contém o nome buscado para o início da lista, de forma que ele possa ser
# encontrado mais rapidamente na próxima vez que for buscado.

class ListaEx03(LinkedList):
    def __init__(self, nodes=None):
        super().__init__(nodes)

    def search(self, node):
        try:
            self.remove_node(node.data)
            self.add_first(node)
            print(f"Site: {node.data} encontrado!")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    print('Exercício 03 da Lista de Exercícios 02')

    lista = ListaEx03(["www.uol.com.br"])
    lista.add_last(Node("www.facebook.com"))
    lista.add_last(Node("www.twitter.com"))
    print(lista)

    lista.search(Node("www.google.com"))
    lista.search(Node("www.twitter.com"))

    print(lista)