# Rock Paper Scissors

from random import choice,seed

choices = ['rock','paper','scissors']

def computer_player():
    '''return a random selection from the 3 options.
    DO NOT CHANGE THIS CODE'''
    return choice(choices)


def human_player():
    '''prompt and return a human selection from the 3 options.'''
    choice = str(input("rock, paper, or scissors?\n"))
    # return choice
    # pass
    
    
def outcome(player1, player2):
    '''return win, lose, or draw for the player1.'''
    if player1 == 'rock' and player2 == 'scissors':
        outcome = 'win'
        return outcome

        
    elif player1 == 'paper' and player2 == 'rock':
        outcome = 'win'
        return outcome
    # pass
    
    elif player1 == 'scissors' and player2 == 'paper':
        outcome = 'win'
        return outcome
        # pass
        
    elif player1 == player2:
        outcome = 'draw'
        return outcome
        # pass
        
    else:
        outcome = 'lose'
        return outcome


def main():
    # determine player choices
    human = human_player()
    computer = computer_player()
    # print human outcome computer
    print(human, outcome(human,computer), computer)
    

# Do not modify the following code or your tests will fail.
'''DO NOT CHANGE THIS CODE'''
if __name__ == '__main__':
    seed(42)
    main()