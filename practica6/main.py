# main.py

import tkinter as tk
from tkinter import messagebox
from game_logic import *
from q_learning import *

CELL_SIZE = 80

BG_COLOR = "#1e1e2f"
BOARD_COLOR = "#2d2d44"
EMPTY_COLOR = "#f1f1f1"
PLAYER_COLOR = "#ffd166"
AI_COLOR = "#ef476f"

class Connect4GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Conecta 4 IA")
        self.root.configure(bg=BG_COLOR)
        self.show_menu()

    def show_menu(self):
        self.clear_window()

        frame = tk.Frame(self.root, bg=BG_COLOR)
        frame.pack(expand=True)

        tk.Label(frame, text="CONECTA 4", font=("Arial", 32, "bold"),
                 fg="white", bg=BG_COLOR).pack(pady=30)

        self.diff_var = tk.StringVar(value="Medio")
        tk.OptionMenu(frame, self.diff_var, "Fácil", "Medio", "Difícil").pack()

        tk.Button(frame, text="Jugar", command=self.start_game).pack(pady=10)
        tk.Button(frame, text="Salir", command=self.root.quit).pack()

    def start_game(self):
        self.difficulty = self.diff_var.get()
        self.clear_window()

        self.board = create_board()

        self.canvas = tk.Canvas(self.root,
                                width=COLS * CELL_SIZE,
                                height=(ROWS + 1) * CELL_SIZE,
                                bg=BG_COLOR)
        self.canvas.pack()

        self.draw_board()
        self.canvas.bind("<Button-1>", self.click)

    def clear_window(self):
        for w in self.root.winfo_children():
            w.destroy()

    def draw_board(self):
        self.canvas.delete("all")

        for r in range(ROWS):
            for c in range(COLS):
                x0 = c * CELL_SIZE
                y0 = (r + 1) * CELL_SIZE
                x1 = x0 + CELL_SIZE
                y1 = y0 + CELL_SIZE

                self.canvas.create_rectangle(x0, y0, x1, y1, fill=BOARD_COLOR)

                piece = self.board[r][c]

                color = EMPTY_COLOR
                if piece == 1:
                    color = AI_COLOR
                elif piece == 2:
                    color = PLAYER_COLOR

                self.canvas.create_oval(x0+10, y0+10, x1-10, y1-10, fill=color)

    def click(self, event):
        col = event.x // CELL_SIZE

        if is_valid_location(self.board, col):
            drop_piece(self.board, col, 2)

            if check_win(self.board, 2):
                messagebox.showinfo("Resultado", "Ganaste")
                self.show_menu()
                return

            self.draw_board()
            self.root.after(300, self.ai_move)

    def ai_move(self):
        state = board_to_string(self.board)
        valid = get_valid_locations(self.board)

        if self.difficulty == "Fácil":
            action = random.choice(valid)
        elif self.difficulty == "Medio":
            action = random.choice(valid) if random.random() < 0.5 else choose_action(state, valid)
        else:
            action = choose_action(state, valid)

        drop_piece(self.board, action, 1)

        if check_win(self.board, 1):
            messagebox.showinfo("Resultado", "La IA gana")
            self.show_menu()
            return

        self.draw_board()


# EJECUCIÓN
load_q()

root = tk.Tk()
root.geometry("600x650")
app = Connect4GUI(root)
root.mainloop()