# UNIVERSIDADE ESTADUAL DO MARANHÃO - UEMA
# MESTRADO PROFISSIONAL EM ENGENHARIA DA COMPUTAÇÃO E SISTEMAS
# ALUNO: FERNANDO DA SILVA PONTES
# PROFESSOR: LUIS CARLOS FONSECA

import math

# Faça um Programa que mostre a mensagem "Alo mundo" na tela. 
print("##### 1 #####")
print('Alô mundo')

# Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número]. 
print("\n")
print("##### 2 #####")
number = int(input('Digite um número: '))
print("O número informado foi %d" % number)

# Faça um Programa que peça dois números e imprima a soma. 
print("\n")
print("##### 3 #####")
number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
print("A soma é igual a %d" % (number1 + number2))

# Faça um Programa que peça as 4 notas bimestrais e mostre a média. 
print("\n")
print("##### 4 #####")
grade1 = float(input('Digite a primeira nota: '))
grade2 = float(input('Digite a segunda nota: '))
grade3 = float(input('Digite a terceira nota: '))
grade4 = float(input('Digite a quarta nota: '))
print("A média é igual a %5.1f" % ((grade1 + grade2 + grade3 + grade4) / 4))

# Faça um Programa que converta metros para centímetros. 
print("\n")
print("##### 5 #####")
meter = float(input('Digite a quantidade de metros: '))
print("{:.2f} metro(s) corresponde a {:.2f} centímetro(s)".format(meter, meter*100))

# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 
print("\n")
print("##### 6 #####")
radius = float(input('Digite o raio do círculo: '))
print("A área do círculo é {:.2f}".format(math.pi * (radius ** 2)))

# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário. 
print("\n")
print("##### 7 #####")
side = float(input('Digite o valor do lado do quadrado: '))
print("A área do quadrado é {:.2f}".format(side ** 2))
print("O dobro da área do quadrado é {:.2f}".format((side ** 2) * 2))

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês. 
print("\n")
print("##### 8 #####")
valueHour = float(input('Digite quanto você ganha por hora: '))
hours = float(input('Digite a quantidade de horas trabalhadas no mês: '))
print("O seu salário é de R$ {:.2f}".format(valueHour * hours))

# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. 
print("\n")
print("##### 9 #####")
degreeFahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
print("A temperatura corresponde a {:.2f}° em Celsius".format(5 * ((degreeFahrenheit - 32) / 9)))

# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit. 
print("\n")
print("##### 10 #####")
degreeCelsius = float(input('Digite a temperatura em Celsius: '))
print("A temperatura corresponde a {:.2f}° em Fahrenheit".format(degreeCelsius * (9/5) + 32))

# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 1 - o produto do dobro do primeiro com metade do segundo.
# 2 - a soma do triplo do primeiro com o terceiro.
# 3 - o terceiro elevado ao cubo. 
print("\n")
print("##### 11 #####")
number1 = int(input('Digite um número inteiro: '))
number2 = int(input('Digite outro número inteiro: '))
number3 = float(input('Digite um número real: '))
print("1 - o produto do dobro do primeiro com metade do segundo: {:.2f}".format((number1*2) * (number2/2)))
print("2 - a soma do triplo do primeiro com o terceiro: {:.2f}".format((number1*3) + number3))
print("3 - o terceiro elevado ao cubo: {:.2f}".format(number3 ** 3))

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58 
print("\n")
print("##### 12 #####")
height = float(input('Digite a sua altura: '))
print("O seu peso ideal deve ser {:.2f} Kg".format((72.7*height) - 58))

# Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, 
# usando a seguinte fórmula: (72.7*altura) - 58 
print("\n")
print("##### 13 #####")
height = float(input('Digite a sua altura: '))
gender = input('Qual o seu sexo (M ou F): ')
if(gender == "M"):
    print("O seu peso ideal deve ser {:.2f} Kg".format((72.7*height) - 58))
elif(gender == "F"):
    print("O seu peso ideal deve ser {:.2f} Kg".format((62.1*height) - 44.7))
else:
    print("Você não digitou M ou F!")

# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. 
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo 
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia 
# a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do 
# limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens 
# adequadas. 
print("\n")
print("##### 14 #####")
weightAllowed = 50.0
weightExceeded = 0.0
weightFeeExceeded = 4.0
feeToBePaid = 0.0
weight = float(input('Digite o peso total do pescado: '))
if(weight > weightAllowed):
    weightExceeded = weight - weightAllowed
    feeToBePaid = weightExceeded * weightFeeExceeded
    print("Você deve pagar uma multa de R$ {:.2f} por {:.2f} kg(s) excedido(s)".format(feeToBePaid, weightExceeded))
else:
    print("O peso total do pescado não ultrapassou os {:.2f} kgs permitidos!".format(weightAllowed))

# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre 
# o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS 
# e 5% para o sindicato, faça um programa que nos dê: 
print("\n")
print("##### 15 #####")
valuePerHour = 0.0
hoursWorked = 0
salary = 0.0
irFee = 11
inssFee = 8
syndicateFee = 5
salaryMinusIrFee = 0.0
salaryMinusInssFee = 0.0
salaryMinusSyndicateFee = 0.0
valuePerHour = float(input('Digite o valor cobrado por hora: '))
hoursWorked = int(input('Digite o quantidade de horas trabalhadas: '))
salary = valuePerHour * hoursWorked
print("+ Salário Bruto : R$ {:.2f}".format(salary))
salaryMinusIrFee = salary * (irFee/100)
print("- IR (11%) : R$ {:.2f}".format(salaryMinusIrFee))
salaryMinusInssFee = salary * (inssFee/100)
print("- INSS (8%) : R$ {:.2f}".format(salaryMinusInssFee))
salaryMinusSyndicateFee = salary * (syndicateFee/100)
print("- SINDICATO (5%) : R$ {:.2f}".format(salaryMinusSyndicateFee))
print("- Salário líquido : R$ {:.2f}".format(salary - salaryMinusIrFee - salaryMinusInssFee - salaryMinusSyndicateFee))

# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 
# litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total. 
print("\n")
print("##### 16 #####")
totalSquareMeter = 0.0
litersPerCan = 18
pricePerCan = 80
litersPerTotalSquareMeter = 0.0
totalCans = 0
totalSquareMeter = float(input('Digite quantos metros quadrados devem ser pintados: '))
litersPerTotalSquareMeter = totalSquareMeter / 3
if(litersPerTotalSquareMeter > litersPerCan):
    totalCans = math.ceil(litersPerTotalSquareMeter / litersPerCan)
else:
    totalCans = 1
print("A quantidade de lata(s) de tinta a serem compradas é {:.2f}".format(totalCans))
print("O preço total a ser pago é R$ {:.2f}".format(totalCans * pricePerCan))

# Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 
# litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. 
print("\n")
print("##### 17 #####")
totalSquareMeter = 0.0
litersPerCan = 18
pricePerCan = 80
litersPerGallon = 3.6
pricePerGallon = 25
litersPerTotalSquareMeter = 0.0
totalCans = 0
totalGallons = 0
totalSquareMeter = float(input('Digite quantos metros quadrados devem ser pintados: '))
litersPerTotalSquareMeter = totalSquareMeter / 6
if(litersPerTotalSquareMeter > litersPerCan):
    totalCans = math.ceil(litersPerTotalSquareMeter / litersPerCan)
else:
    totalCans = 1
print("Comprar apenas latas de 18 litros:")
print("--------------------------------------")    
print("A quantidade de lata(s) de tinta a serem compradas é {:.2f}".format(totalCans))
print("O preço total a ser pago é R$ {:.2f}".format(totalCans * pricePerCan))
print("\n")
if(litersPerTotalSquareMeter > litersPerGallon):
    totalGallons = math.ceil(litersPerTotalSquareMeter / litersPerGallon)
else:
    totalGallons = 1
print("Comprar apenas galões de 3,6 litros:")
print("--------------------------------------")    
print("A quantidade de lata(s) de tinta a serem compradas é {:.2f}".format(totalGallons))
print("O preço total a ser pago é R$ {:.2f}".format(totalGallons * pricePerGallon))
