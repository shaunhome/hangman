# Hangman Game

Welcome to the Hangman Game, implemented in Python!

## Overview
This project is a text-based implementation of the classic Hangman game. Players can enter a word, choose a random word from a predefined list, or have the computer randomly select a word for them. Another player then guesses letters one at a time or attempts to guess the entire word. The game features a visual representation of the hangman's gallows that dynamically updates as incorrect guesses are made. Don't hesitate if the console doesn't show your text: this is intentional. The game uses `getpass` to hide Player 1’s input for secrecy. Just type the word or phrase and press Enter.

## Features
- **Dynamic Hangman Display**: ASCII art representation of the hangman figure evolves with each incorrect guess.
- **Multi-word Support**: Players can input multiple words, guessing entire phrases at once.
- **Error Handling**: Validation ensures input is limited to letters or correct guesses.
- **Language Switch**: Option to switch between languages (English and Welsh) for a localized gaming experience.
- **Random Word Option**: Players can choose to play with a randomly selected word from a predefined list or have the computer select a word.

## Coding Practices
- **Modular Design**: Organized into separate modules for input handling, game logic, display functions, and language management.
- **Error Handling**: Robust validation to handle various user inputs and prevent unexpected errors.
- **ASCII Art**: Utilization of ASCII art for visual representation of the hangman's progression.
- **Interactive Gameplay**: Provides a user-friendly interface with clear instructions and prompts.

## Technologies Used
- **Python**: Core programming language used for game implementation.
- **ASCII Art**: Displaying visual elements within the console.
- **GitHub**: Version control and project management.

## Usage
To play the game:
1. Clone the repository to your local machine.
2. Run `hangman.py` using Python.
3. Choose a word option (user input or random).
4. Follow the on-screen instructions to play Hangman!

## Credits
Developed by Shaun Davies

Enjoy the game and have fun guessing words!

---
