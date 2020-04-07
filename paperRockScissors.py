#PAPER, ROCK, SCISSORS

print("\n\n\nWelcome to Paper, Rock, Scissors")
print("".center(50,"-"))
player1Name = input("Player 1, Enter your Name: ")
player2Name = input("Player 2, Enter your Name: ")
print("".center(50,"-"),'\n\n\n')

player1Move = input(f"Okay...{player1Name} Paper, Rock, or Scissors?\n\tFor Paper type (p)\n\tFor Rock type (r)\n\tFor Scissors type(s)\n")
player2Move = input(f"\n\nOkay...{player2Name} Paper, Rock, or Scissors?\n\tFor Paper type (p)\n\tFor Rock type (r)\n\tFor Scissors type(s)\n\n\n")

if player1Move == 'r' and player2Move == 's':
    print(player1Name+' wins!')
elif player1Move == 'r' and player2Move == 'p':
    print(player2Name+' wins!')
elif player1Move == 'r' and player2Move == 'r':
    print(player1Name + " " + player2Name + ' tie!')


if player1Move == 'p' and player2Move == 'r':
    print(player1Name+' wins!')
elif player1Move == 'p' and player2Move == 's':
    print(player2Name+' wins!')
elif player1Move == 'p' and player2Move == 'p':
    print(player1Name + " " + player2Name + ' tie!')


if player1Move == 's' and player2Move == 'p':
    print(player1Name+' wins!')
elif player1Move == 's' and player2Move == 'r':
    print(player2Name+' wins!')
elif player1Move == 's' and player2Move == 's':
    print(player1Name + " " + player2Name + ' tie!')