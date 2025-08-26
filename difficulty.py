import tkinter as tk

def choose_difficulty(main_form):
    """
    Open a modal dialog asking the player to choose a difficulty level.
    Returns: one of the strings "easy", "medium", or "hard".
    main_form: the root/top-level Tk window that the dialog should be attached to.
    """
    # Use a mutable container so the nested set_choice function can modify the selected value.
    # Default to "medium" if the user closes the window without choosing.
    chosen = {"level": "medium"}

    # Create a new top-level window attached to the main application window.
    diff_win = tk.Toplevel(main_form)
    diff_win.title("Choose Difficulty")

    # Informational label at the top of the dialog.
    tk.Label(diff_win, text="Select Difficulty Level:", font=("Verdana", 14)).pack(pady=10)

    # Buttons for the three difficulty choices. Each button calls set_choice with an argument.
    # Note: set_choice is defined below; we use a lambda to pass the desired difficulty string.
    tk.Button(diff_win, text="Easy", width=10, command=lambda: set_choice("easy")).pack(pady=5)
    tk.Button(diff_win, text="Medium", width=10, command=lambda: set_choice("medium")).pack(pady=5)
    tk.Button(diff_win, text="Hard", width=10, command=lambda: set_choice("hard")).pack(pady=5)

    def set_choice(diff):
        """
        Callback invoked when a difficulty button is pressed.
        Updates the chosen value and closes the dialog.
        """
        chosen["level"] = diff
        diff_win.destroy()

    # Make this dialog modal:
    # - grab_set ensures all events are sent to diff_win until it is destroyed (prevents interacting with main_form).
    # - wait_window blocks execution in the caller until diff_win has been destroyed.
    diff_win.grab_set()
    main_form.wait_window(diff_win)

    # Return the selected difficulty (or the default if user closed dialog otherwise).
    return chosen["level"]