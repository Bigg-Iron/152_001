# 5.12 A5 Program

The Big Bang Theory fans may recognize Rock Paper Scissors Lizard Spock as a game of chance that expands on the standard Rock Paper Scissors game. It introduces two new hand signs and several more rules.

The rules:

- Lizard eats Paper
- Lizard poisons Spock
- Paper covers Rock
- Paper disproves Spock
- Rock crushes Lizard
- Rock crushes Scissors
- Scissors decapitates Lizard
- Scissors cuts Paper
- Spock vaporizes Rock
- Spock smashes Scissors
- In this assignment you will write a program to implement the game so a human player competes against a computer player. This program is extremely similar to Lab 5, you may find it helpful to refer back to it. Like the lab, some code has been provided for you.

This program should:

Prompt the user to input one of the five options: rock, paper, scissors, lizard, or spock?
Determine the outcome (win, lose, or draw) from player1's perspective.
Here are the specifications for the functions you will be writing:

- `human_player()`
  - Takes no parameters.
  - Prompts the user to input rock, paper, scissors, lizard, or spock?
  - Returns the user's selection as a string.
- `outcome(player1, player2)`
  - Takes two parameters, player1 and player2, both are strings
  - Determines the result of the game using if, elif, and/or else statements. There are several different ways to go about this, do whatever you feel is best.
  - Returns win, lose, or draw as a string

Input Example 1:

Note: While testing in develop mode, don't forget to provide the program with input values in the smaller box below.

`spock`

Output Example 1:

`rock, paper, scissors, lizard, or spock?
spock win rock`

When testing your code, the computer_player/player2 will always choose rock. This is by design. If you'd like to actually play this game you can remove the seed function from main and it will pick random choices. Make sure you put the seed(42) back in to get full points.
