# Hangman Game in Python

# Overview:

This project is a User Interface graphical focused Hangman game implemented using Python and the Tkinter library. It offers a classic hangman game experience, where the user guesses the word using letters one at a time to uncover a hidden word. The interface of the game is built with Tkinter, providing a visually engaging and interactive platform for users to play the game. The game draws from a list of random words each time, ensuring a varied experience and allowing for continuous replay-ability. The player must guess the word by selecting letters and is allowed a limited number of incorrect guesses before the game concludes; just like in the actual game of Hangman.
This project was designed for the casual gamer audience or anyone interested in developing and utilizing a GUI-based application. This project leverages Python's GUI capabilities to provide a fun and engaging user experience.

# Features:
-	Graphical User Interface built with Tkinter for interactive gameplay
-	Random word selection from a sizeable, predefined list, which will allow for continuous replay-ability, and preventing users from just guessing the word at the start of the game
-	Displays the game board, guesses, correct letters guessed, and remaining lives to the user
-	Clickable button-based and keyboard enterable letter selection for guesses
-	In classic Hangman style, the game ends when the word is guessed correctly or the player runs out of available unused lives/guesses

## Technologies Used:
-	Python 3.11
-	Tkinter
-	Standard Python libraries (string, random, os)

# Usage Instructions:

# File Pathway Tree/ File Directory:

\Python-Hangman-Game\
| --- main.py

## Installation & Setup:
1.	Clone this repository to your local machine. Ensure that Python 3.11 is installed inside of a runnable IDE (Such as PyCharm).
2.	Make sure that the Tkinter library, along with the rest of the more common Python libraries (string, random, os) are downloaded and installed.
3.	After that there are no additional downloads/libraries required; just run the “main.py” script directly.

## Running And Playing the Game:
1.	Launch the game by executing the main.py python script.
2.	A window will open displaying the Hangman game interface. The game board displays blanks representing each letter of the word.
3.	Click on the alphabet buttons that are on the interface display or type the letter/character you are aiming to guess.
4.	The game updates the board with correct guesses, revealing positions of the letter in the word; or decreases remaining lives for incorrect guesses.
5.	Play continues until the word is fully guessed or no lives remain, where the game ends, and you are prompted to exit or play again.

# Contributing to the Codebase:
Contributions are welcome! Feel free to fork, modify, and submit pull requests to improve and expand upon functionality of the game or fix any errors/bugs found with the game. Your contributions help make the game better and more enjoyable for everyone!
