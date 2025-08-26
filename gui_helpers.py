import tkinter as tk
import string

# Will be assigned by main.py for global access to main window
main_form = None

# -------------------- Update Display Labels --------------------
def update_display(game, gui_gameboard, gui_guess_archive, gui_lives):
    """Refresh the labels to show current game state."""
    gui_gameboard.config(text=" ".join(game.gameboard))
    gui_guess_archive.config(text=" ".join(game.guess_archive))
    gui_lives.config(text=f'Lives({game.lives_remaining}):')

# -------------------- Handle Letter Button Click --------------------
def button_click(game, button, gui_helpers, gui_gameboard, gui_guess_archive, gui_lives):
    """Handle click on a letter button."""
    letter = button.cget('text').lower()
    button.config(state="disabled")  # Disable button after click
    game.get_user_guess(letter, gui_helpers, gui_gameboard, gui_guess_archive, gui_lives, button)

# -------------------- Populate Keyboard --------------------
def populate_board(game, keyboard_frame, button_dict, gui_helpers, gui_gameboard, gui_guess_archive, gui_lives):
    """Create buttons for letters a-z and organize them in rows."""
    alpha_list = list(string.ascii_lowercase)
    rows, cols = 3, 9
    index = 0
    for r in range(rows):
        # Last row has fewer letters; center it
        letters_in_row = cols if r < 2 else 26 - 2*cols
        start_col = (cols - letters_in_row)//2
        for c in range(letters_in_row):
            if index < 26:
                letter = alpha_list[index].upper()
                button = tk.Button(
                    keyboard_frame,
                    text=letter,
                    width=4,
                    height=2,
                    command=lambda b=letter: button_click(
                        game, button_dict[b],
                        gui_helpers, gui_gameboard, gui_guess_archive, gui_lives
                    )
                )
                button.grid(row=r, column=start_col+c, padx=2, pady=2)
                button_dict[letter] = button
                index += 1

# -------------------- Draw Hangman --------------------
def draw_hangman(game):
    """Draw hangman on canvas based on remaining lives."""
    canvas = game.canvas
    canvas.delete("all")  # Clear previous drawing

    # Base coordinates for drawing
    x, y = 200, 50

    # Draw base and stand
    canvas.create_line(x-130, 250, x+20, 250, width=3)  # Base
    canvas.create_line(x-80, 250, x-80, y, width=3)      # Pole
    canvas.create_line(x-80, y, x, y, width=3)           # Beam
    canvas.create_line(x, y, x, y+40, width=3)           # Rope

    # Determine number of parts to draw based on difficulty and lives
    parts_total = game.hangman_parts_count()
    drawn = parts_total - game.lives_remaining - 1

    head = (x-20, y+40, x+20, y+80)
    torso_top = y+80
    torso_bottom = y+140
    steps = []

    # -------------------- Drawing Steps by Difficulty --------------------
    if game.difficulty == "easy":
        steps = [
            lambda: canvas.create_oval(*head, width=3),  # Head
            lambda: canvas.create_line(x, torso_top, x, torso_bottom, width=3),  # Torso
            lambda: canvas.create_line(x, y+100, x-30, y+120, width=3),  # Left leg
            lambda: canvas.create_line(x, y+100, x+30, y+120, width=3),  # Right leg
            lambda: canvas.create_line(x, torso_bottom, x-20, torso_bottom+40, width=3),  # Left arm
            lambda: canvas.create_line(x, torso_bottom, x+20, torso_bottom+40, width=3),  # Right arm
            lambda: [canvas.create_oval(x-10, y+50, x-5, y+55),  # Left eye
                     canvas.create_oval(x+5, y+50, x+10, y+55)],  # Right eye
            lambda: [canvas.create_line(x, y+55, x, y+65),  # Mouth
                     canvas.create_arc(x-10, y+60, x+10, y+70, start=0, extent=-180)]  # Smile
        ]
    elif game.difficulty == "medium":
        steps = [
            lambda: canvas.create_oval(*head, width=3),
            lambda: canvas.create_line(x, torso_top, x, torso_bottom, width=3),
            lambda: [canvas.create_line(x, y+100, x-30, y+120, width=3),
                     canvas.create_line(x, y+100, x+30, y+120, width=3)],
            lambda: [canvas.create_line(x, torso_bottom, x-20, torso_bottom+40, width=3),
                     canvas.create_line(x, torso_bottom, x+20, torso_bottom+40, width=3)],
            lambda: [canvas.create_oval(x-10, y+50, x-5, y+55),
                     canvas.create_oval(x+5, y+50, x+10, y+55),
                     canvas.create_line(x, y+55, x, y+65),
                     canvas.create_arc(x-10, y+60, x+10, y+70, start=0, extent=-180)],
            lambda: None
        ]
    else:  # Hard
        steps = [
            lambda: canvas.create_oval(*head, width=3),
            lambda: canvas.create_line(x, torso_top, x, torso_bottom, width=3),
            lambda: [canvas.create_line(x, y+100, x-30, y+120, width=3),
                     canvas.create_line(x, y+100, x+30, y+120, width=3)],
            lambda: [canvas.create_line(x, torso_bottom, x-20, torso_bottom+40, width=3),
                     canvas.create_line(x, torso_bottom, x+20, torso_bottom+40, width=3),
                     canvas.create_oval(x-10, y+50, x-5, y+55),
                     canvas.create_oval(x+5, y+50, x+10, y+55),
                     canvas.create_line(x, y+55, x, y+65),
                     canvas.create_arc(x-10, y+60, x+10, y+70, start=0, extent=-180)]
        ]

    # Draw only as many steps as required
    for i in range(min(drawn, len(steps))):
        step = steps[i]
        if callable(step):
            step()