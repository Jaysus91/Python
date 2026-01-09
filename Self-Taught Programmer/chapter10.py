# Building hangman
def hangman(word):
    wrong_guess=0
    stages=[ "" , "________ " , "| | " , "| 0" , "| /|\ " , "| / \ " , "| " ]
    letters_left=list(word)
    score_board=['_']*len(word)
    win=False
    print('Welcome to Hang Man')

    while wrong_guess < len(stages)-1:
        print('\n')
        guess=input("Guess a letter")
        if guess in letters_left:
            character_index=letters_left.index(guess)
            score_board[character_index]=guess
            letters_left[character_index]='$'
        else:
            wrong_guess+=1
        print("".join(score_board))
        print('\n'.join(stages[0:wrong_guess+1]))
        if '_' not in score_board:
            print('You win! the word was:')
            print(''.join(score_board))
            win=True
            break
        if not win:
            print('\n'.join(wrong_guess[0:stages]))
            print('You lose! The word was {}'.format(word))
hangman("charlie")        