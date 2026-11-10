# Jargon Jumble

## Project Overview
Jargon Jumble is a tech-themed word scramble game. The user is shown a shuffled word and a hint, and they must guess the original word. The game tracks the score, gives hints, lets the user skip or quit, and displays a final result at the end.

This project introduces game logic and interactive programming in Python.

## Python Concepts Learned
- `random` module for choosing words and shuffling letters
- Lists and tuples to store the word bank and game data
- `while` loops to keep the game running over multiple rounds
- `if`, `elif`, and `else` statements for game decisions
- `input()` for player interaction
- `.strip().lower()` to clean and normalize user input
- Score tracking with variables
- `break` to stop the game when the player quits
- Basic game-state management using arrays and conditions

## Example
A round may show:
- `Shuffle word is: ntdbeu`
- Hint: "I spent four hours trying to debug my code. Turns out I was missing a comma."

The player then tries to guess the correct word, such as `debug`.
