from random import randint
from time import sleep
from itertools import permutations

global opp1cards
global opp2cards

cards = []
player1 = []
player2 = []
ty1 = 1
ty2 = 1
opp1cards = 13
opp2cards = 13
player1move = 0
player2move = 0
rounds = 69
round_num = 0
drawcards = 'y'
player1score = 0
player2score = 0
global gamedata
gamedata = []
gamelist = []
reps = 0
enum = 1
counter = 0
datawrite = 'n'

def prepare(opp1_cards, opp2_cards, repetitions):
    if repetitions != 0:
        opp1cards = []
        opp2cards = []

        for i in range(13^(opp1_cards + opp2_cards) * repetitions)
        if enum >= repetitions:
            counter =+ 1
            enum = 1
        else:
            enum += 1
        a = round(counter % 13)
        b = round((counter % 169 - a)/13)
        c = round((counter % 2197 - b)/169)
        opp1cards.append([a, b])
        opp2cards.append([c])    


def initiate(opp1_cards, opp2_cards):
    global cards
    global player1
    global player2

    cards = []
    player1 = []
    player2 = []
    # Resets the variables

    for i in range(2, 15):
        for x in range(4):
            cards.append(i)
    # This initiates the deck.

    if type(opp1_cards) == 'list':
        for i in opp1_cards:
            player1.append(cards.pop(cards.index(i)))
    else:
        for i in range(opp1_cards):
            player1.append(cards.pop(random.randint(0, len(cards) -1)))
    if type(opp2_cards) == 'list':
        for i in opp2_cards:
            player2.append(cards.pop(cards.index(i)))
    else:
        for i in range(opp2_cards):
            player2.append(cards.pop(random.randint(0, len(cards) -1)))
    # If the variable is a list, it uses the terms from the list to create a player hand. Otherwise, it uses the variable to determine the amount of cards dealt randomly.
  
 

def opponent1_move(type):
    global player1
    global player1move
    if type == 1:
        player1move = player1.pop(random.randint(0, len(player1)-1))
    if type == 2:
        player1.sort()
        player1move = player1.pop(0)
    if type == 3:
        player1.sort()
        player1move = player1.pop(len(player1)-1)

def opponent2_move(type):
    global player2
    global player2move
    if type == 1:
        player2move = player2.pop(random.randint(0, len(player2)-1))
    if type == 2:
        player2.sort()
        player2move = player2.pop(0)
    if type == 3:
        player2.sort()
        player2move = player2.pop(len(player2)-1)


def evaluation(draw_cards):
    if player1move != player2move:
        if (player1move != 2 or player2move != 2) and (player1move != 14 or player2move != 14):
            if player1move > player2move:
                player1.append(player2move)
                if len(cards) != 0 and draw_cards != "n":
                    player1.append(cards.pop(random.randint(0, len(cards)-1)))

                        
            else:
                player2.append(player1move)
                if len(cards) != 0 and draw_cards != "n":
                    player2.append(cards.pop(random.randint(0, len(cards)-1)))
        else:
            if player1move == 2:
                player1.append(player2move)
                if len(cards) != 0 and draw_cards != "n":
                    player1.append(cards.pop(random.randint(0, len(cards)-1)))
            else:
                player2.append(player1move)
                if len(cards) != 0 and draw_cards != "n":
                    player2.append(cards.pop(random.randint(0, len(cards)-1)))

def gameplay:
    initiate(opp1_cards, opp2_cards)
    opponent1_move(int(ty1))
    opponent2_move(int(ty2))
    evaluation(drawcards)
    


##################################################################################################################

print("The CardGame v1.1 program has launched. Please enter the specified desired parameters, below.")
rounds = int(input("How many rounds would you want to simulate? "))
command = input("Do you want to access settings? y/n: ")
time.sleep(1)

if command == "y":
    print("Accessing settings...")
    time.sleep(0.5)
    ty1 = int(input("Opponent 1 type: "))
    opp1cards = int(input("Opponent 1 card amount: "))
    ty2 = int(input("Opponent 2 type: "))
    opp2cards = int(input("Opponent 2 card amount: "))
    command = input("Do you want to access advanced settings? y/n: ")
    if command == "y":
        drawcards = input("Draw cards? y/n: ")
        reps = int(input("Enumeration reps (0 for no): "))
        datawrite = input("Do you want to write gameplay data to CardGameData.txt? y/n: ")
        print("The settings have been inputted.")
    time.sleep(0.5)
print("The program will initiate shortly.")
time.sleep(2)

prepare(opp1cards, opp2cards, reps)

for i in range(rounds):
    x = i
    initiate(opp1_cards, opp2_cards)
    while len(player1) != 0 and len(player2) != 0:
        gamedata.append([player1, player2])
        opponent1_move(int(ty1))
        opponent2_move(int(ty2))
        evaluation(drawcards)
    if len(player1) > len(player2):
        player1score += 1
    elif len(player1) < len(player2):
        player2score += 1
    else:
        player1score += 0.5
        player2score += 0.5
    print(str(i + 1) + " out of " + str(rounds) + " matches: " + str(player1score) + "-" + str(player2score))
    if datawrite == 'y':
        with open("CardGameData.txt", "a+") as CGData:
            CGData.seek(0)
            test1 = CGData.read(100)
            if len(test1) > 0:
                CGData.write("\n")
                CGData.write("\n")
            CGData.write("Player 1 cardset: " + str(gamedata[0]))
            CGData.write("\n")
            CGData.write("Player 2 cardset: " + str(gamedata[1]))
            CGData.write("\n")
            CGData.write("Gameplay: " + str(gamedata[2:-1]))
            gamedata = []
        
print("")
print("Player 1 had a score of " + str(player1score) + " and Player 2 had a score of " + str(player2score) + "!")
