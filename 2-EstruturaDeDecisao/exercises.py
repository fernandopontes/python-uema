# UNIVERSIDADE ESTADUAL DO MARANHÃO - UEMA
# MESTRADO PROFISSIONAL EM ENGENHARIA DA COMPUTAÇÃO E SISTEMAS
# ALUNO: FERNANDO DA SILVA PONTES
# PROFESSOR: LUIS CARLOS FONSECA 

# Faça um Programa que peça dois números e imprima o maior deles. 
print("\n")
print("##### 1 #####")

number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))

if(number1 > number2):
    print("O maior número é {:.1f}".format(number1))
else:
    print("O maior número é {:.1f}".format(number2))

# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.
print("\n")
print("##### 2 #####") 
number1 = int(input('Digite um número positivo ou negativo: '))

if(number1 > 0):
    print("O número {:.1f} é positivo".format(number1))
else:
    print("O número {:.1f} é negativo".format(number1))

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
# Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido. 
print("\n")
print("##### 3 #####") 
gender = input('Digite (M) para Masculino ou (F) para feminino: ').upper()
if(gender == "M"):
    print("Masculino")
elif(gender == "F"):
    print("Feminino")
else:
    print("Sexo inválido")

# Faça um Programa que verifique se uma letra digitada é vogal ou consoante. 
print("\n")
print("##### 4 #####") 
letter = input('Digite a letra: ').lower()
if(letter in "aeiou"):
    print("A letra '{0}' é uma vogal".format(letter))
else:
    print("A letra '{0}' é uma consoante".format(letter))