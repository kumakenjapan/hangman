#Chapter 10
#Hangman game

def hangman(word):
    wrong = 0 #How many times of error
    stages = ["",
              "__________        ",
              "|         |       ",
              "|         O       ",
              "|        /|)      ",
              "|        / )      ",
              "|     Game Over!   "
             ]

    reletters = list(word)
    board = ["_"] * len(word) #Show hints
    win = False #Game status
    print("Welcome to hangman game!")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Please guess one character."
        char = input(msg)
        if char in reletters:
            cind = reletters.index(char)
            board[cind] = char
            reletters[cind] = '$'

        else:
            wrong += 1

        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break

    if not win:
        print("\n".join(stages[0:wrong+1]))
        print("You lose! The answer is {}".format(word))


hangman("dog")
