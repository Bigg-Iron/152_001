# Rock Paper Scissors Lizard Spock

from random import choice,seed

def computer_player():
    '''return a random selection from the 5 options.'''
    return choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])


def human_player():
    '''prompt and return a human selection from the 5 options.'''
    humanPlayer_choice = str(input('choose your character: rock, paper, scissors, lizard, or spock \n'))
    
    return(str(humanPlayer_choice))
    # pass


def outcome(player1, player2):
    '''return win, lose, or draw for the player1.'''
    
    pass


def main():
    # determine player choices
    human = human_player()
    computer = computer_player()
    # print human outcome computer
    print(human, outcome(human,computer), computer)
    

# Do not modify the following code or your tests will fail.
if __name__ == '__main__':
    seed(42)
    main()