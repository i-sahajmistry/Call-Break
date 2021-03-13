from src import *

score = [0, 0, 0, 0]
roundNumber = 0
while True:
    deck = shuffledDeck()
    players = distributeCards(deck)
    convertToNumber(players)
    userCards = players[0]
    print(f'Yor are Player 0. \nYour Cards are : \n {showUserCards(userCards)}\n')
    calls = makeCall()
    print(f'Calls made by each Player : {calls}')
    firstPlayer = score.index(max(score))
    currentPlayer = firstPlayer
    subRound = [0, 0, 0, 0]

    for _ in range(13):
        if _ != 0:
            currentPlayer = subRoundWinner
        for i in range(4):
            throwCard(currentPlayer, players, userCards)
            currentPlayer += 1
            if currentPlayer % 4 == 0:
                currentPlayer = 0
        for i in range(4):
            pass
            #print(len(players[i]))
        subRoundWinner = checkWinner()
        subRound[subRoundWinner] += 1
        showCardsOnTable()
        print(f'Subround winner : {subRoundWinner}\n')
        print(f'Number of Hands won : {subRound} ')
        currentPlayer = subRoundWinner
        clearTable()

    for i in range(4):
        if calls[i] <= subRound[i]:
            if calls[i] < 8:
                score[i] += calls[i]
            else:
                score[i] += 13
        else:
            score[i] -= calls[i]

    roundNumber += 1
    print(f'Scores after round {roundNumber} : {score}')
    winnerScore = max(score)
    winnerIndex = score.index(winnerScore) + 1
    print(f'Winner of {roundNumber} round is Player {winnerIndex} with score {winnerScore}\n')
    print('Do you Want to play next round? ([y]/n) : ')
    z = playAgain()
    if z == 'n':
        break
    else:
        pass
