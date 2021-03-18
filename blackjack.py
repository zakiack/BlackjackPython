import tkinter as tk
import numpy
puntees = open("totalpoints.txt", "r")
playerMoney = float(puntees.read())
betMoney = 0
puntees.close()
playerCards = []
dealerCards = []
ableToHit = False
ableToStay = False
ableToBet = True
class card:
    name = "cardname"
    value = 0
cards = []
Ace = card()
Ace.name = "Ace"
Ace.value = 1
cards.append(Ace)

two = card()
two.name = "Two"
two.value = 2
cards.append(two)

three = card()
three.name = "Three"
three.value = 3
cards.append(three)

four = card()
four.name = "Four"
four.value = 4
cards.append(four)

five = card()
five.name = "Five"
five.value = 5
cards.append(five)

six = card()
six.name = "Six"
six.value = 6
cards.append(six)

seven = card()
seven.name = "Seven"
seven.value = 7
cards.append(seven)

eight = card()
eight.name = "Eight"
eight.value = 8
cards.append(eight)

nine = card()
nine.name = "Nine"
nine.value = 9
cards.append(nine)

ten = card()
ten.name = "Ten"
ten.value = 10
cards.append(ten)

queen = card()
queen.name = "Queen"
queen.value = 10
cards.append(queen)

king = card()
king.name = "King"
king.value = 10
cards.append(king)

jack = card()
jack.name = "Jack"
jack.value = 10
cards.append(jack)
def restart():
    global ableToHit
    global ableToStay
    global ableToBet
    global playerCards
    global dealerCards
    playerCards = []
    dealerCards = []
    mainWindow.update()
    ableToHit = False
    ableToStay = False
    ableToBet = True
    betBox.config(text="Bet", command=bet)
    message.config(text="Enter a bet")

def updateFile():
    global playerMoney
    f = open("totalpoints.txt","w")
    f.write(str(playerMoney))
    f.close()

def calcTotalValue(deck):
    total = 0
    for i in deck:
        total += i.value
    return total

def createCardString(deck):
    names = ""
    for i in deck:
        newNames = names+i.name+", "
        names = newNames
    return names

def loose():
    global ableToHit
    global ableToStay
    global betMoney
    ableToStay = False
    ableToHit = False
    points.config(text="Money: $" + str(playerMoney))
    updateFile()
    message.config(text="haha idiot you lost $"+str(betMoney))
    betBox.config(text="Play again",command=restart)

def win():
    global ableToHit
    global ableToStay
    global playerMoney
    global betMoney
    ableToStay = False
    ableToHit = False
    playerMoney += (2*betMoney)
    betMoney = 0
    updateFile()
    points.config(text="Money: $" + str(playerMoney))
    message.config(text="you won $"+str(betMoney)+" good job")
    betBox.config(text="Play again", command=restart)

def dealerLoop():
    cardnum = numpy.random.randint(0,len(cards))
    dealerCards.append(cards[cardnum])
    dealerLabel.config(text="Dealer Cards: "+createCardString(dealerCards))
    totalValue = calcTotalValue(dealerCards)
    playerVal = calcTotalValue(playerCards)
    if 21 >= totalValue > playerVal:
        loose()
    elif totalValue <= 16:
        dealerLoop()
    elif 21 >= totalValue > 16:
        if playerVal > totalValue:
            win()
        else:
            loose()
    elif totalValue > 21:
        win()

def hit():
    global ableToHit
    if ableToHit:
        cardNum = numpy.random.randint(0,len(cards))
        playerCards.append(cards[cardNum])
        cardLabel.config(text="Cards: "+createCardString(playerCards))
        total = calcTotalValue(playerCards)
        if total > 21:
            loose()
def stay():
    global ableToHit
    global ableToStay
    if ableToStay:
        val = calcTotalValue(playerCards)
        message.config(text="You have a total of "+str(val))
        ableToHit = False
        dealerLoop()

def bet():
    global playerMoney
    global ableToBet
    global betMoney
    global ableToHit
    global ableToStay
    if ableToBet:
        moners = float(betEntry.get())
        if moners <= playerMoney:
            playerMoney = playerMoney - moners
            betMoney = moners
            points.config(text="Money: $"+str(playerMoney))
            ableToHit = True
            ableToStay = True
            ableToBet = False
            message.config(text="Hit or Stay?")
            cardLabel.config(text="Cards: " + createCardString(playerCards))


mainWindow = tk.Tk()
mainWindow.title("Blackjack")
title = tk.Label(mainWindow,text="Blackjack!",font=("Arial",40))
title.grid(row=0,column=0)
points = tk.Label(mainWindow,text="Money: $"+str(playerMoney),anchor="w")
points.grid(row=1,column=0)
cardLabel = tk.Label(mainWindow,text="Cards: "+createCardString(playerCards),anchor="w")
cardLabel.grid(row=1,column=1)
dealerLabel = tk.Label(mainWindow,text="Dealer Cards: "+createCardString(dealerCards),anchor="w")
dealerLabel.grid(row=2,column=0)
HitButton = tk.Button(mainWindow,text="Hit",command=hit)
HitButton.grid(row=3,column=0)
stayButton = tk.Button(mainWindow,text="Stay",command=stay)
stayButton.grid(row=3,column=1)
betBox = tk.Button(mainWindow,text="Bet",command=bet)
betBox.grid(row=4,column=0)
betEntry = tk.Entry(mainWindow)
betEntry.grid(row=4,column=1)
message = tk.Label(mainWindow,text="Enter a bet")
message.grid(row=5,column=0)
mainWindow.mainloop()
