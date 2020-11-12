import random

cards = []
player1 = []
player2 = []
ty = 0
player1_move = 0
player2move = 0

def prepare():
    for i in range(2, 15):
        for x in range(4):
            cards.append(i)

    for i in range(13):
        player1.append(cards.pop(random.randint(0, len(cards) -1)))
        player2.append(cards.pop(random.randint(0, len(cards) -1)))
    
    print("Welcome to the Card Game! Type exit to exit and rules for the rules of the game.")
    player1_move = input("Need to know the rules?: ")
    if player1_move == "yes":
            print("Here are the rules: Higher numbers beat lower numbers. The only exception is when 14 is matched up against 2, which in this case 2 wins to prevent 14 to be overpowered. After people play their cards, the winner gets the other person's lower card and the higher card is discarded into the waste pile. Then the person who won draws a card from the draw pile, if there is a card still there. If you tie, the card gets added to the pot and the stakes get higher! It will continue until someone beats another. When a winner is declared after a showdown, the person takes all the loser's card and the winner takes the same number of cards he won from the draw pile. For example, if you win after tying once, then you get the loser's two cards and draw two more cards, if available.")
    player1_move = 0

def player_move():
    global player1_move
    print("These are your cards.")
    print(player1)
    player1_move = (input("Input what you want to play:"))
    
    try:    
        if (int(player1_move) in player1):
            player1_move = int(player1_move)
        else:
            if player1_move == "exit":
                pass
            else:
                while not player1_move in player1:
                    player1_move = int(input("Input not valid. Please try again:"))
    except:
        while not player1_move in player1 or not player1_move == "exit":
            player1_move = int(input("Input not valid. Please try again:"))
    
    if player1_move in player1:
        player1_move = player1.pop(player1.index(player1_move))

def opponent_move(type):
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
    print("Player 2 drew a " + str(player2move) + "!")


def evaluation():
    if player1_move != player2move and not player1_move == "exit":
        if player1_move > player2move:
            player1.append(player2move)
            print("You win! You take Player's 2 card.")
            if len(cards) != 0:
                player1.append(cards.pop(random.randint(0, len(cards)-1)))
                print("You also take a card from the deck. You get a " + str(player1[len(player1)-1]) + "!")
                        
        else:
            player2.append(player1_move)
            print("You lose! Player 2 takes your card.")
            if len(cards) != 0:
                player2.append(cards.pop(random.randint(0, len(cards)-1)))
                print("Player 2 also takes a card from the deck.")
    elif player1_move == player2move:
        print("It is a tie! The two cards are added to the pot and the winner of the next round takes all!")
        player_move()
        opponent_move(int(ty))
        evaluation()
        
    else:
        print("The game will be exited.")
    
    print("")
    if not player1_move == "exit" and len(cards) % 5 == 0 or len(cards) == 1:
        if not len(cards) == 0:
            print("There are " + str(len(cards)) + " cards left in the draw deck.")
        else:
            print("There are no more cards left in the deck.")


##################################################################################################################



prepare()
ty = input("Opponent type: ")
while len(player1) != 0 and len(player2) != 0 and player1_move != "exit": 
    player_move()
    opponent_move(int(ty))
    evaluation()

print("The game is finished.")
if len(player1) > len(player2):
    print("Congratulations! You have won the game against the computer!")
else:
    print("The computer has won. Would you like to play again another time?")
