import random
from lista import Node
from lista import CircularLinkedList

# Ex. 06:
# 1 - sorteia um número
# 2 - inicia a contagem por um soldado aleatorio
# 3 - a contagem é realizada até o número sorteado
# 4 - onde a contagem parou, o soldado é removido do círculo
# 5 - volta para a etapa 1
# 6 - recomeça a contagem no soldado seguinte ao que foi eliminado
# 7 - tem um vetor de tamanho 10
# 8 - números para sorteiar: -9 a 9
# 9 - valores negativos fazem a contagem andar para a esquerda
# 10 - valores positivos fazem a contagem andar para a direita
# 11 - 0 não é válido no sorteio e deve ser realizado um novo sorteio
# 12 - cada soldado deve ter um valor único

class ListaEx06(CircularLinkedList):
    soldiers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def __init__(self):
        super().__init__(self.soldiers)

    def hat_of_draw(self):
        number_of_draw = random.randint(-9, 9)
        return self.hat_of_draw() if number_of_draw == 0 else number_of_draw

    def soldier_of_draw(self):
        number_of_draw = random.choice(self.soldiers) 
        if(number_of_draw > 0):
            return number_of_draw
        else:
            self.soldier_of_draw()            

    def remove_soldier_circle(self):
        while len(self.soldiers) > 1:
            number_break = self.hat_of_draw()
            start_point = self.soldier_of_draw()
            way = "left" if number_break > 0 else "right"
            if start_point is None:
                    start_point = self.head
            else:
                start_point = self.search_node(start_point)
            node = start_point.next if way == "left" else start_point.previous
            i = 1
            while node is not None and (node != self.head):
                if i == abs(number_break):
                    if(node.data == 0):
                        self.remove_soldier_circle()
                    else:
                        start_point = node.next.data
                        if(start_point == 0):
                            start_point = random.choice(self.soldiers) 
                        index = self.soldiers.index(node.data)
                        del self.soldiers[index]
                        self.remove_node(node.data)
                        break
                node = node.next if way == "left" else node.previous
                i += 1
    
    def raffle(self):
        self.remove_soldier_circle()
        print(f'O soldado escolhido é: {self.soldiers}')
        
if __name__ == '__main__':
    print('Exercício 06 da Lista de Exercícios 02')

    lista = ListaEx06()
    lista.raffle()