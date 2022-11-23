import random

p1 = input("Rock, paper or scissors?").lower()
p2 = random.randint(1, 3)

rock = 1
paper = 2
scissor = 3

if p1 == p2:
    print("Its  a draw")
elif p1 == 1 and p2 == 2:
    print("Player 2 went for paper. You lose")
elif p1 == 1 and p2 == 3:
    print("Player 2 went for scissors. You win")
elif p1 == 2 and p2 == 3:
    print("Player 2 went for scissors. You lose")
elif p1 == 2 and p2 == 3:
    print("Player 2 went for rock. You win")
elif p1 == 3 and p2 == 1:
    print("Player 2 went for rock. You lose")
elif p1 == 3 and p2 == 2:
    print("Player 2 went for paper. You win")
else:
    print("Enter either rock paper or scissors")



