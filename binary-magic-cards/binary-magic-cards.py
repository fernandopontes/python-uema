# UNIVERSIDADE ESTADUAL DO MARANHÃO - UEMA
# MESTRADO PROFISSIONAL EM ENGENHARIA DA COMPUTAÇÃO E SISTEMAS
# ALUNO: FERNANDO DA SILVA PONTES
# PROFESSOR: LUIS CARLOS FONSECA

def defineTotalNumber(totalNumberCards):
    exponent = totalNumberCards - 1;
    quantityNumberPerCard = 2**exponent;
    totalNumbers = quantityNumberPerCard * 2 - 1
    return totalNumbers  

def defineCards(totalNumberCards, totalNumbers):
    cards = {}
    i = 0
    while(i < totalNumberCards):
        firstNumberList = 2**i
        interval = firstNumberList
        card = []

        z = firstNumberList
        countNumber = 1
        while(z <= totalNumbers):
            card.append(z)
            if(countNumber == interval):
                z+=interval+1
                countNumber = 1
            else:
                z+=1
                countNumber+=1

        cards[i+1] = card
        i+=1
    return cards

def guess(cards):
    result = 0
    for card in cards:
        response = input(f'O número está neste card? (S/N) -> {cards[card]}: ')
        if(response.upper() == "S"):
            result += cards[card][0]
    print("\n")
    print("----------------------------------------")
    print(f"Você pensou no número: {result}")

if __name__ == '__main__':
    print('#### JOGO DOS CARTÕES MÁGICOS BINÁRIOS ####')
    print("\n")
    totalNumberCards = int(input('Digite a quantidade de cartões que você deseja: '))
    totalNumbers = defineTotalNumber(totalNumberCards)
    cards = defineCards(totalNumberCards, totalNumbers)
    print("\n")
    print("Os cartões gerados são:")
    print("----------------------------------------")
    for card in cards:
        print('CARTÃO ' + str(card) + ":")
        print(cards[card])
        print("\n")
    print(f'Pense em um número entre 1 e {totalNumbers}...')
    thought = input('E ai, já pensou? (S/N) ')
    if thought.upper() != "S":
        print('Pois pense logo!')
    else:
        print('Não vai esquecer o número...')

    guess(cards)