import random
import sys


print("Welcome to RPS!")
moves: dict = {"r": 'rock', "p": "paper", "s": "scissors"}
valid_moves: list[str] = list(moves.keys())


while True:
    user_move = input("Rock(r), paper(p), or scissors(s) and (e) to quit? ").lower()


    if user_move == "e":
        print("Thanks for playing")
        sys.exit()
    

    if user_move not in valid_moves:
        print("Invalid move")
        continue


    # AI Decision
    ai_move = random.choice(valid_moves)

    print("-----------------------------")
    print(f"You: {moves[user_move]}")
    print(f"AI: {moves[ai_move]}")
    print("-----------------------------")

    
    # Check moves
    if moves[user_move] == moves[ai_move]:
        print("It is a tie!")
    elif moves[user_move] == "rock" and moves[ai_move] == "scissors":
        print("You won!")
    elif moves[user_move] == "scissors" and moves[ai_move] == "paper":
        print("You won!")
    elif moves[user_move] == "paper" and moves[ai_move] == "rock":
        print("You won!")
    else:
        print("AI won!")


