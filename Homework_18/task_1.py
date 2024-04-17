import random

def random_symbol():
    symbols=["R","P","S"]
    return random.choice(symbols)
    
def main():
    user_score = 0
    comp_score = 0

    while True:
        if user_score == 3 or comp_score ==3:
            break

        user_choice = input("Enter the symbol: ").upper()
        comp_choice = random_symbol()
        print(comp_choice)

        if user_choice == comp_choice:
            print("No winner")

        elif (user_choice == "R" and comp_choice == "S"):
            print("You win")
        elif (user_choice == "S" and comp_choice == "P"):
             print("You win")
        elif (user_choice == "P" and comp_choice == "R"):
            print("You win")
            user_score = user_score + 1
        
        else:
            print("Computer win")
            comp_score = comp_score + 1
        
        if user_score == 3:
            print("You are winner of game")
            break
        elif comp_score == 3:
            print("Compuer is winner of game")
            break
        
if __name__ == "__main__":
    main()
