from random import choice, randint

global cardsOnTable, FIRST
cardsOnTable = {}


def shuffledDeck():
    index = ['A'] + [i for i in range(2, 11)] + ['J', 'Q', 'K']
    suit = ['♥', '♦', '♠', '♣']
    cards = {str(i)+j for i in index for j in suit}
    return list(cards)


def distributeCards(deck):
    players = [[], [], [], []]
    for i in range(52):
        player = i % 4
        card = choice(deck)
        players[player].append(card)
        deck.remove(card)
    return players


def convert(i):
    if i[0:2] == '10':
        toNumber = ['10', i[2]]
    elif i[0] == 'A':
        toNumber = ['14', i[1]]
    elif i[0] == 'J':
        toNumber = ['11', i[1]]
    elif i[0] == 'Q':
        toNumber = ['12', i[1]]
    elif i[0] == 'K':
        toNumber = ['13', i[1]]
    else:
        toNumber = [str(i[0]), i[1]]
    return toNumber


def convertToNumber(players):
    for j in range(len(players)):
        temp = players[j].copy()
        for i in temp:
            toNumber = convert(i)
            players[j].remove(i)
            players[j].append(toNumber)


def arrangeCards(userCards):
    suit = {'♠': [], '♣': [], '♥': [], '♦': []}
    for i in userCards:
        if i[0:2] == '10':
            suit[i[2]].append(i[0:2])
        else:
            suit[i[1]].append(i[0])
    for i in suit:
        suit[i].sort()
    showCards = [j+i for i in suit for j in suit[i]]
    return showCards


def showUserCards(userCards):
    showCards = []
    for i in userCards:
        if i[0] == '11':
            showCards.append('J' + i[1])
        elif i[0] == '12':
            showCards.append('Q' + i[1])
        elif i[0] == '13':
            showCards.append('K' + i[1])
        elif i[0] == '14':
            showCards.append('A' + i[1])
        else:
            showCards.append(i[0] + i[1])
    return arrangeCards(showCards)


def makeCall():
    calls = []
    while True:
        try:
            n = int(input("Make a Call(between 1-13) : "))
            if 0 < n < 14:
                calls.append(n)
                break
        except ValueError:
            pass
    for i in range(3):
        n = randint(1, 7)
        calls.append(n)
    return calls


def currentSuit():
    global cardsOnTable
    if cardsOnTable[FIRST][0:2] == '10':
        return cardsOnTable[FIRST][2]
    else:
        return cardsOnTable[FIRST][1]


def showCardsOnTable():
    if not cardsOnTable:
        print('\nThrow First Card : ')
    else:
        print(f'\nCards on table : {cardsOnTable}')


def throwCard(currentPlayer, players, userCards):
    global cardsOnTable, FIRST
    if len(cardsOnTable) == 0:
        FIRST = currentPlayer
    if currentPlayer == 0:
        showCardsOnTable()
        x = showUserCards(userCards)
        print('\n', x)
        while True:
            card = input("Copy paste card from above to throw : ")
            card = list(card)
            while "'" in card:
                card.remove("'")
            card = ''.join(card)

            if card in x:
                if not cardsOnTable:
                    card = convert(card)
                    userCards.remove(card)
                    cardsOnTable[currentPlayer] = card
                    break
                elif cardsOnTable:
                    flag = 0
                    for i in userCards:
                        if (i[0:2] != '10' and i[1] == currentSuit()) \
                                or (i[0:2] == '10' and i[2] == currentSuit()):
                            flag = 1
                            break
                    if flag == 1:
                        if (card[0:2] != '10' and card[1] == currentSuit()) \
                                or (card[0:2] == '10' and card[2] == currentSuit()):
                            card = convert(card)
                            userCards.remove(card)
                            cardsOnTable[currentPlayer] = card
                            break
                    else:
                        card = convert(card)
                        userCards.remove(card)
                        cardsOnTable[currentPlayer] = card
                        break
            print('Invalid Selection...')

    else:
        if not cardsOnTable:
            flag = 0
            for card in players[currentPlayer]:
                if card[1] != '♠':
                    cardsOnTable[currentPlayer] = card
                    players[currentPlayer].remove(card)
                    flag = 1
                    break
            if flag == 0:
                card = choice(players[currentPlayer])
                cardsOnTable[currentPlayer] = card
                players[currentPlayer].remove(card)

        else:
            suit = currentSuit()
            flag = 0
            for card in players[currentPlayer]:
                if card[1] == suit:
                    cardsOnTable[currentPlayer] = card
                    players[currentPlayer].remove(card)
                    flag = 1
                    break
            if flag == 0:
                card = choice(players[currentPlayer])
                cardsOnTable[currentPlayer] = card
                players[currentPlayer].remove(card)


def checkWinner():
    global cardsOnTable
    cardIndex = []
    suits = []
    for i in cardsOnTable:
        if cardsOnTable[i][0:2] == '10':
            cardIndex.append('10')
            suits.append(i[2])
        else:
            cardIndex.append(cardsOnTable[i][0])
            suits.append(cardsOnTable[i][1])

    if '♠' in suits:
        x = '♠'
    else:
        x = currentSuit()

    winnerIndex = suits.index(x)
    winnerCardIndex = cardIndex[winnerIndex]
    for i in range(4):
        if suits[i] == x and int(cardIndex[i]) > int(winnerCardIndex):
            winnerCardIndex = cardIndex[i]
    winnerCard = [winnerCardIndex, x]
    for i in cardsOnTable:
        if cardsOnTable[i] == winnerCard:
            return i


def clearTable():
    global cardsOnTable
    cardsOnTable = {}


def playAgain():
    while True:
        z = input().lower()
        if z == 'n' or 'no':
            return 'n'
        elif z == 'y' or 'yes':
            return 'y'
