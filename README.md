# Hangman Game in Python (Tkinter)
# Overview
This project is a fully interactive Hangman game built using Python and the Tkinter library. It provides a graphical user interface where players can guess letters to reveal a hidden word before running out of lives. The application features multiple difficulty levels, a dynamic on-screen keyboard, but still allows the user to guess through typing letters with keys, it showcases a visual hangman drawing that updates with incorrect guesses, and a hint system to assist players if needed.
This Hangman Game has a user-centric focused design, allowing users of all skill levels to have fun and enjoy the game. This project demonstrates the use of GUI programming, event handling, and game logic all inside of Python. It also highlights interactive design principles such as visual feedback, difficulty scaling, and entices the user to want to come back and continue replaying the game.

# Features
-	**Difficulty Levels** – Easy, Medium, and Hard difficulty options affect word length and available lives/guesses, adding a challenge to the game and allowing users of any skill level to be able to enjoy the game.
-	**On-Screen & Physical Keyboard Input** – Guess letters by clicking the visual keyboard or typing with your real keyboard.
-	**Dynamic Gameboard** – The length of the word is represented with underscores, updating automatically with correct guesses.
-	**Lives System** – Allows the user to have a limited number of wrong guesses (different per difficulty) before losing.
-	**Hangman Drawing** – A stick figure is drawn step by step for each incorrect guess to expand on the visual aspects of the game.
-	**Hint System** – A button is present that allows the user the option to reveal the first letter of the word, informing the user if the first letter is already being displayed; thus no hints are available to be displayed.
-	**Replay Support** – Prompt to restart the game with difficulty selection after each win/loss.
-	**Color Feedback** – Correct guesses are highlighted with the color green, meanwhile incorrect guesses are highlighted red.

## Technologies Used
-	Python 3.11
-	Tkinter (Python Standard GUI Library)
-	Random Module (for word selection)
-	Standard Python libraries (string, random, os)

# Usage Instructions

# File Pathway Tree/ File Directory:

\Python-Hangman-Game\
| --- main.py\
| --- difficulty.py\
| --- gui_helpers.py\
| --- hangman.py

## Installation & Setup
1.	Clone this repository to your local machine. Ensure that Python 3.11 is installed inside of a runnable IDE (Such as PyCharm).
2.	Make sure that the Tkinter library, along with the rest of the more common Python libraries (string, random, os) are downloaded and installed.
3.	After that there are no external downloads/libraries are required (Tkinter comes bundled with Python); just run the “main.py” script directly.

## Running the Game
1.	From the project directory, run: the main.py file inside of this repository
2.	A window will launch prompting you to select a difficulty level (Easy, Medium, or Hard).
3.	After selecting which difficulty you want, you can start guessing letters by clicking the on-screen buttons or using your keyboard to type in your letter guesses.
4.	The game updates the board with correct guesses, revealing positions of the letter in the word and coloring the letter guessed green ; or decreases remaining lives for incorrect guesses and greys out the letter on the virtual keyboard and changes the color of the letter to red. Additionally, the hangman drawing will progress with each incorrect guess until you are at zero or guess the word correctly.
5.	Use the Hint button if you get stuck to show the first letter of the word, or inform the user if the first letter has been guessed already and thus a hint is not available.
6.	After a win or loss, you can choose to restart the game with a new difficulty level or exit.
________________________________________
## How It Works
-	**Word Selection:** Randomly chosen from difficulty-based word lists.
-	**Gameboard:** Underscores represent unknown letters, which is updated as the player guesses correctly.
-	**Lives & Hangman Image Drawing:** Each wrong guess reduces lives and adds a new part to the hangman drawing.
-	**Win/Loss Conditions:**\
o	 Win if all letters are revealed.\
o	 Lose if lives reach zero and the word is fully revealed.
-	**Replayability:** After each game is completed, win or lose, players can choose to restart with a difficulty of their choice or exit the game.
________________________________________
# Contributing to the Codebase
Contributions are welcome! Feel free to fork the repository, suggest improvements, or add features. Please submit pull requests with clear descriptions of your changes after developing your changes.
