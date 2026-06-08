
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a Hangman game in Python that uses loops, conditionals, string handling, and user input so players can guess a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️ Word Selection and Progress Display

#### Description

Create a function to select a random word and show the current guessed progress with underscores for hidden letters.

#### Requirements
Completed program should:

- Choose a random word from a predefined list
- Display the word progress using underscores for letters that have not been guessed yet
- Reveal correct letters in the progress display as they are guessed

### 🛠️ Guess Handling and Game Logic

#### Description

Implement the main gameplay loop to accept guesses, update game state, and track remaining attempts.

#### Requirements
Completed program should:

- Accept single-letter guesses from the user
- Update the displayed word progress after each guess
- Deduct an attempt for incorrect guesses
- End the game when the word is guessed or the player runs out of attempts

### 🛠️ Win/Lose Results

#### Description

Add final messaging to tell the player whether they won or lost and reveal the correct word.

#### Requirements
Completed program should:

- Display a win message when the player guesses the word
- Display a lose message when the player runs out of attempts
- Reveal the correct word when the game ends
