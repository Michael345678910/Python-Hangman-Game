import random
import tkinter as tk
from tkinter import messagebox

class Hangman:
    # -------------------- Initialize Hangman Game --------------------
    def __init__(self, difficulty="medium", canvas=None, keyboard_frame=None, button_dict=None, difficulty_func=None):
        # -------------------- Game State Variables --------------------
        self.difficulty = difficulty
        self.played_word = ""  # Current word to guess
        self.gameboard = []  # List of letters and underscores representing progress
        self.gameboard_finished = []  # Full word for win condition checks
        self.guess_archive = ['Guesses:']  # Letters guessed so far
        self.lives_remaining = self.set_lives()  # Lives based on difficulty
        self.end_state = False  # True if game is over (win or lose)

        # -------------------- GUI References --------------------
        self.canvas = canvas  # Reference to the drawing canvas
        self.keyboard_frame = keyboard_frame  # Frame containing letter buttons
        self.button_dict = button_dict  # Dictionary mapping letters to Button widgets

        # Function to allow difficulty selection when resetting the game
        self.choose_difficulty_func = difficulty_func

        # -------------------- Word Lists for Difficulty Levels --------------------
        self.easy_words = ['cat','dog','sun','cup','map','bat','pen','hat','fan','jar',
                           'box','key','toy','car','sky','pie','net','bag','rat','wig',
                           'log','tip','lid','arm','ice']
        self.medium_words = ['apple','banana','grape','orange','table','chair','brush','plant',
                             'shirt','house','mouse','spoon','clock','water','light','phone',
                             'pencil','paper','plate','glove','candy','bread','shirt','shirt','bread']
        self.hard_words = ['elephant','computer','building','mountain','triangle','notebook',
                           'keyboard','language','dinosaur','pineapple','adventure','painting',
                           'hospital','butterfly','umbrella','mosquito','strawberry','difficult',
                           'beautiful','pinecone','chocolate','volcano','squirrel','penguin','internet']

        # -------------------- Initialize Game --------------------
        self.set_word()  # Select a word randomly based on difficulty
        self.create_gameboard(self.played_word)  # Fill gameboard with underscores
        self.set_finished_board(self.played_word)  # Store the full word

    # -------------------- Lives Handling --------------------
    def set_lives(self):
        """Return number of lives based on difficulty."""
        if self.difficulty == "easy": return 8
        elif self.difficulty == "hard": return 4
        return 6

    def hangman_parts_count(self):
        """Return total number of hangman parts for drawing."""
        return self.set_lives()

    # -------------------- Word Selection --------------------
    def set_word(self):
        """Randomly select a word from the appropriate difficulty list."""
        if self.difficulty == "easy": candidates = self.easy_words
        elif self.difficulty == "medium": candidates = self.medium_words
        else: candidates = self.hard_words
        self.played_word = random.choice(candidates)

    def set_finished_board(self, word):
        """Store the complete word as a list for comparison with gameboard."""
        self.gameboard_finished = list(word)

    def create_gameboard(self, word):
        """Initialize gameboard with underscores for each letter."""
        self.gameboard = ['_'] * len(word)

    # -------------------- Update Gameboard --------------------
    def update_move(self, guess, location):
        """Update the gameboard at a specific index with a correct guess."""
        self.gameboard[location] = guess

    # -------------------- Process Player Guesses --------------------
    def process_guess(self, player_guess, gui_helpers, gui_gameboard, gui_guess_archive, gui_lives, button=None):
        """Handle logic for a guessed letter, update lives, and refresh UI."""
        if player_guess in self.guess_archive:
            messagebox.showinfo("Repeated Guess", f"You have already tried '{player_guess}'!")
            return

        if player_guess in self.gameboard_finished:
            # Correct guess: reveal letter(s) in the gameboard
            for i, char in enumerate(self.gameboard_finished):
                if char == player_guess:
                    self.update_move(player_guess, i)
            self.guess_archive.append(player_guess)
            if button:
                button.config(bg="green", disabledforeground="white")  # Visual feedback for correct guess
            gui_helpers.update_display(self, gui_gameboard, gui_guess_archive, gui_lives)
            self.check_game_status(gui_helpers, gui_gameboard, gui_guess_archive, gui_lives)
        else:
            # Incorrect guess: decrement lives and update hangman drawing
            if self.lives_remaining > 0:
                self.lives_remaining -= 1
                self.guess_archive.append(player_guess)
                gui_helpers.draw_hangman(self)
                if button:
                    button.config(bg="red", disabledforeground="white")  # Visual feedback for wrong guess
                gui_helpers.update_display(self, gui_gameboard, gui_guess_archive, gui_lives)
                self.check_game_status(gui_helpers, gui_gameboard, gui_guess_archive, gui_lives)

    # -------------------- Check Win/Lose Conditions --------------------
    def check_game_status(self, gui_helpers, gui_gameboard, gui_guess_archive, gui_lives):
        """Determine if the player has won, lost, or should continue."""
        if self.lives_remaining == 0:
            self.end_state = True
            if messagebox.askyesno(
                "Game Over",
                f"Game Over! You ran out of lives.\nAnswer: {''.join(self.gameboard_finished)}\nDo you want to play again?"
            ):
                if self.choose_difficulty_func:
                    self.reset_game(gui_helpers, gui_gameboard, gui_guess_archive, gui_lives, self.choose_difficulty_func)
                else:
                    self.reset_game(gui_helpers, gui_gameboard, gui_guess_archive, gui_lives)
            else:
                gui_helpers.main_form.quit()
        elif self.gameboard == self.gameboard_finished:
            self.end_state = True
            if messagebox.askyesno("Congratulations!", "You won! Do you want to play again?"):
                if self.choose_difficulty_func:
                    self.reset_game(gui_helpers, gui_gameboard, gui_guess_archive, gui_lives, self.choose_difficulty_func)
                else:
                    self.reset_game(gui_helpers, gui_gameboard, gui_guess_archive, gui_lives)
            else:
                gui_helpers.main_form.quit()

    # -------------------- Handle Input --------------------
    def get_user_guess(self, letter, gui_helpers, gui_gameboard, gui_guess_archive, gui_lives, button=None):
        """Validate input and forward to guess processing."""
        if len(letter) == 1 and letter.isalpha():
            self.process_guess(letter.lower(), gui_helpers, gui_gameboard, gui_guess_archive, gui_lives, button)

    # -------------------- Reset Game --------------------
    def reset_game(self, gui_helpers, gui_gameboard, gui_guess_archive, gui_lives, difficulty_func=None):
        """Reset all game state to start a new round."""
        if difficulty_func:
            self.difficulty = difficulty_func()
        self.set_word()
        self.create_gameboard(self.played_word)
        self.set_finished_board(self.played_word)
        self.guess_archive = ['Guesses:']
        self.lives_remaining = self.set_lives()
        self.end_state = False

        # Clear canvas drawing
        self.canvas.delete("all")
        gui_helpers.update_display(self, gui_gameboard, gui_guess_archive, gui_lives)

        # Reset keyboard buttons
        for widget in self.keyboard_frame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(state="normal", bg="SystemButtonFace")

    # -------------------- Hint Function --------------------
    def use_hint(self, gui_helpers, gui_gameboard, gui_guess_archive, gui_lives):
        """Reveal the first letter of the word if it hasn't been guessed yet."""
        first_letter = self.gameboard_finished[0]
        if first_letter not in self.guess_archive:
            button = self.button_dict.get(first_letter.upper())
            self.process_guess(first_letter, gui_helpers, gui_gameboard, gui_guess_archive, gui_lives, button)
            if button:
                button.config(state="disabled")
        else:
            messagebox.showinfo("Hint Used", "The first letter has already been revealed!")