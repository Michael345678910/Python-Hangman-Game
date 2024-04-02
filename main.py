import string
import random
import os
import tkinter as tk
from tkinter import messagebox, OUTSIDE

class Hangman:
    played_word = ""
    gameboard = []
    gameboard_finished = []
    guess = ''
    guess_archive = ['Guesses:']
    lives = ['Lives(5):']
    end_state = False
    word_list = ['stun', 'amuse', 'comment', 'systematic', 'adviser', 'argument', 'chemistry', 'ward', 'goal', 'knot', 'confession', 'desk', 'opinion', 'dilute', 'horoscope', 'number', 'overall', 'dark', 'girl', 'association', 'reserve', 'shrink', 'autonomy', 'worker', 'confrontation', 'mountain', 'conception', 'corpse', 'prestige', 'family', 'belief', 'mobile', 'trouble', 'temptation']

    def set_word(self):
        word = random.choice(self.word_list)
        self.played_word = word

    def set_finished_board(self, word):
        self.gameboard_finished = list(word)

    def create_gameboard(self, word):
        self.gameboard = ['_'] * len(word)

    def update_move(self, guess, location):
        self.gameboard[location] = guess

    def process_guess(self, player_guess):
        if player_guess in self.guess_archive:
            print("You have already tried to play " + player_guess)
        elif player_guess in self.gameboard_finished:
            for position, char in enumerate(self.gameboard_finished):
                if char == player_guess:
                    self.update_move(player_guess, position)
            self.guess_archive.append(player_guess)
        else:
            self.lives.append('x')
            self.guess_archive.append(player_guess)

    def check_game_status(self):
        if(len(self.lives) == 6):
            os.system('cls' if os.name == 'nt' else 'clear')
            self.end_state = True
            messagebox.showinfo("GAME OVER!", f"GAME OVER: Thanks for playing! \n Answer: {''.join(self.gameboard_finished)}")
            main_form.quit()
        elif(self.gameboard == self.gameboard_finished):
            os.system('cls' if os.name == 'nt' else 'clear')
            self.end_state = True
            messagebox.showinfo("Congrats!", "You won! Thanks for playing!")
            main_form.quit()

    def get_user_guess(self, letter):
        if(len(letter) == 1 and letter.isalpha()):
            self.process_guess(letter.lower())
        else:
            print("Guess must be a single letter!")

game = Hangman()
game.set_word()
game.create_gameboard(game.played_word)
game.set_finished_board(game.played_word)

main_form = tk.Tk()
main_form.title("Hangman")
main_form.geometry("600x310")
main_form.resizable(0, 0)

alpha_list = list(string.ascii_lowercase)

gui_gameboard = tk.Label(main_form, text=game.gameboard, font="Verdana 30 bold")
gui_gameboard.pack(side="top")

gui_guess_archive = tk.Label(main_form, text=game.guess_archive, font="Verdana 10 bold")
gui_guess_archive.pack()
gui_guess_archive.place(bordermode=OUTSIDE, x=200, y=260)

gui_lives = tk.Label(main_form, text=game.lives, font="Verdana 10 bold")
gui_lives.pack()
gui_lives.place(bordermode=OUTSIDE, x=200, y=280)

def button_click(letter):
    letter.config(state="disabled")
    game.get_user_guess(letter.cget('text').lower())
    gui_gameboard['text'] = game.gameboard
    gui_guess_archive['text'] = game.guess_archive
    gui_lives['text'] = game.lives
    game.check_game_status()

def create_button(letter, xpos, ypos, index):
    button = tk.Button(main_form, text=alpha_list[index].upper(), command=lambda: button_click(button))
    button.pack()
    button.place(bordermode=OUTSIDE, height=50, width=100, x=xpos, y=ypos)

def populate_board():
    c = 0
    startpos = 60
    xpos = 0
    ypos = startpos
    for c in range(26):
        if c % 6 == 0 and c != 0:
            ypos += 50
            xpos = 0
        create_button(alpha_list[c], xpos, ypos, c)
        xpos += 100

populate_board()
main_form.mainloop()
