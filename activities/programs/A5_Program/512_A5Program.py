from random import choice,seed

def computer_player():
    '''return a random selection from the 5 options.'''
    return choice(['rock', 'paper', 'scissors', 'lizard', 'spock'])


def human_player():
    '''prompt and return a human selection from the 5 options.'''
    humanPlayer_choice = str(input('rock, paper, scissors, lizard, or spock?\n'))
    
    return(str(humanPlayer_choice))
    # pass


def outcome(player1, player2):
    '''return win, lose, or draw for the player1.'''
    if player1 == 'lizard' and player2 == 'paper':
        outcome = 'win'
        return outcome

        
    elif player1 == 'lizard' and player2 == 'spock':
        outcome = 'win'
        return outcome
    
    # elif player2 == 'lizard' and player1 == 'spock':
    #     outcome = 'lose'
    #     return outcome
        
    elif player1 == 'paper' and player2 == 'rock':
        outcome = 'win'
        return outcome
    
    elif player1 == 'paper' and player2 == 'spock':
        outcome = 'win'
        return outcome
        
    elif player1 == 'rock' and player2 == 'lizard':
        outcome = 'win'
        return outcome
        
    elif player1 == 'rock' and player2 == 'scissors':
        outcome = 'win'
        return outcome
        
    elif player1 == 'scissors' and player2 == 'lizard':
        outcome = 'win'
        return outcome
        
    elif player1 == 'scissors' and player2 == 'paper':
        outcome = 'win'
        return outcome
        
    elif player1 == 'spock' and player2 == 'rock':
        outcome = 'win'
        return outcome
        
    elif player1 == 'spock' and player2 == 'scissors':
        outcome = 'win'
        return outcome
        
    elif player1 == player2:
        outcome = 'draw'
        return outcome
    
    else:
        outcome = 'lose'
        return outcome
        
    # return player1, player2
    # pass


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