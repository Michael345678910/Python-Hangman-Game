import tkinter as tk
from hangman import Hangman
import gui_helpers as gui_helpers
from difficulty import choose_difficulty

# -------------------- Main GUI --------------------
# Create main window for the application
main_form = tk.Tk()
main_form.title("Hangman")
main_form.geometry("600x700")
main_form.resizable(0, 0)

# Provide a reference to the main form to gui_helpers so helpers can access it (used to quit the app)
gui_helpers.main_form = main_form  # link to GUI helpers

# Frames and Canvas ----------------------------------------------------------
# Top frame holds the drawing canvas for the hangman
top_frame = tk.Frame(main_form)
top_frame.pack(side="top", pady=10)

# Middle frame holds text labels (gameboard, guesses, lives)
middle_frame = tk.Frame(main_form)
middle_frame.pack(side="top", pady=10)

# Keyboard frame holds the letter buttons
keyboard_frame = tk.Frame(main_form)
keyboard_frame.pack(side="top", pady=10)

# Canvas used to draw the hangman parts
gui_canvas = tk.Canvas(top_frame, width=400, height=300, bg="white")
gui_canvas.pack()

# Difficulty selection ------------------------------------------------------
# Wrap choose_difficulty in a lambda so we can pass it into Hangman and call it later when resetting.
difficulty_func = lambda: choose_difficulty(main_form)
# Immediately prompt the user to choose a difficulty before starting the game
difficulty = difficulty_func()

# Button dictionary ---------------------------------------------------------
# Will map uppercase letters (e.g. 'A') to their corresponding Button widget.
button_dict = {}

# Hangman game instance -----------------------------------------------------
# Instantiate the Hangman game logic and provide GUI references so it can update the UI.
game = Hangman(difficulty=difficulty, canvas=gui_canvas,
               keyboard_frame=keyboard_frame, button_dict=button_dict,
               difficulty_func=difficulty_func)

# Labels -------------------------------------------------------------------
# Label that displays the current state of the word (e.g. "_ _ a _")
gui_gameboard = tk.Label(middle_frame, text=game.gameboard, font="Verdana 30 bold")
gui_gameboard.pack()

# Label that displays the list of guesses the player has made
gui_guess_archive = tk.Label(middle_frame, text=" ".join(game.guess_archive), font="Verdana 10 bold")
gui_guess_archive.pack()

# Label that displays remaining lives
gui_lives = tk.Label(middle_frame, text=f'Lives({game.lives_remaining}):', font="Verdana 10 bold")
gui_lives.pack()

# Keyboard -----------------------------------------------------------------
# Populate the keyboard_frame with letter buttons and fill button_dict for lookup
gui_helpers.populate_board(game, keyboard_frame, button_dict, gui_helpers,
                           gui_gameboard, gui_guess_archive, gui_lives)

# Key press bindings -------------------------------------------------------
def key_press(event):
    # Capture the character from the keyboard event and normalize to lowercase
    letter = event.char.lower()
    # Only handle alphabetic single-character keys (a-z)
    if letter in 'abcdefghijklmnopqrstuvwxyz':
        # Process the guess through the game logic (no associated button passed here)
        game.get_user_guess(letter, gui_helpers, gui_gameboard, gui_guess_archive, gui_lives)
        # Refresh the displayed labels after processing the guess
        gui_helpers.update_display(game, gui_gameboard, gui_guess_archive, gui_lives)
        # If the corresponding on-screen button exists, disable it to reflect the used key
        if letter.upper() in button_dict:
            button_dict[letter.upper()].config(state="disabled")

# Bind all key presses on the main window to the key_press handler
main_form.bind('<Key>', key_press)

# Hint button --------------------------------------------------------------
# Provide a button that reveals the first letter of the word (if not already revealed).
# It calls Hangman.use_hint, which will handle updating the UI and disabling the button.
hint_button = tk.Button(
    main_form,
    text="Hint",
    font=("Verdana", 12, "bold"),
    bg="yellow",
    width=8,
    command=lambda: game.use_hint(gui_helpers, gui_gameboard, gui_guess_archive, gui_lives)
)
hint_button.pack(pady=10)

# Initial display update --------------------------------------------------
# Ensure the labels reflect the initial game state (underscores, lives, guesses)
gui_helpers.update_display(game, gui_gameboard, gui_guess_archive, gui_lives)

# Start the Tkinter main event loop ----------------------------------------
# This call blocks and hands control to Tkinter until the window is closed.
main_form.mainloop()
