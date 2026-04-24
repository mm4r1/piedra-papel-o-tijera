from logic import options, choose_computer, decide_winner

continue_game = True

print("welcome to the game!")

while continue_game:
    games = int(input("how many rounds would you like to play?: "))
    score1 = 0
    score2 = 0
    while True:
        print("\nchoose your option")
        print("rock, paper or scissors")
        player = input("enter your option: ").lower().strip()

        while player not in options:
            print("error. invalid option")
            player = input("enter your option: ").lower().strip()
    
        computer = choose_computer()
        print("the computer chose: ", computer)

        result = decide_winner(player, computer)
        if result == "tie":
            print("Tie")
        elif result == "win":
            print("You win!")
            score1 += 1
        else:
            print("You lost :(")
            score2 += 1
    
        print(f"score || player: {score1} | computer: {score2}")
    
        if score1 == games:
            print("congratulations! you have won the game!! :D")
            break
        elif score2 == games:
            print("the computer has won the game :(")
            break
        
    print("do you want to keep playing?")
    print("1. yes \n2. no")
    continue1 = input("choose an option: ").strip()
    while continue1 not in ["1", "2"]:
        print("error. invalid option")
        print("do you want to keep playing?")
        print("1. yes \n2. no")
        continue1 = input("choose an option: ").strip()
    if continue1 == "2":
        print("see you later!")
        continue_game = False