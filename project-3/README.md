# Sing Out

## Project Overview
Sing Out is a karaoke queue manager. It keeps track of singers and songs in a queue, allows users to add or remove singers, move someone to the top, show the next performer, and close the queue.

This project teaches how to build a small interactive app with persistent in-memory data and commands.

## Python Concepts Learned
- Lists of tuples to store singer/song pairs
- Functions to organize code into reusable blocks
- `enumerate()` to display the queue with numbered entries
- `if` statements to validate commands and queue conditions
- User input handling with `input()`
- String cleaning with `.strip().title()`
- App loops with `while` to keep the program running
- List operations such as `append()`, `pop()`, `remove()`, and `insert()`
- Basic validation, such as checking for empty names, missing queue entries, and invalid input

## Example
The app may display a queue like:
- 1. Annie - Dancing Queen
- 2. Allen - Country Roads

The user can type commands such as:
- `add`
- `remove`
- `next`
- `top`
- `quit`

This creates a simple command-driven menu system.
