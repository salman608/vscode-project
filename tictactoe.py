import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")
        master.configure(bg="#f0f0f0")  # Light background

        self.board = [""] * 9
        self.current_player = "X"
        self.game_over = False
        self.cell_size = 100  # Size of each cell in pixels
        self.line_width = 8    # width of the X and O outlines
        self.canvas = tk.Canvas(master, width=self.cell_size * 3, height=self.cell_size * 3, bg="white", highlightthickness=0)  # White background for the board
        self.canvas.pack(padx=20, pady=20) # padding around the board

        self.canvas.bind("<Button-1>", self.canvas_click)  # Bind click event to the canvas

        self.draw_grid()

    def draw_grid(self):
        for i in range(1, 3):  # Draw two vertical and two horizontal lines
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.cell_size * 3, width=3, fill="black") # Vertical lines
            self.canvas.create_line(0, i * self.cell_size, self.cell_size * 3, i * self.cell_size, width=3, fill="black") # Horizontal Lines

    def canvas_click(self, event):
        if self.game_over:
            return

        x = event.x // self.cell_size
        y = event.y // self.cell_size
        index = y * 3 + x

        if self.board[index] == "":
            self.board[index] = self.current_player
            self.draw_move(index, self.current_player)

            if self.check_win():
                messagebox.showinfo("Game Over", f"{self.current_player} wins!")
                self.game_over = True
            elif self.check_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def draw_move(self, index, player):
        x = (index % 3) * self.cell_size
        y = (index // 3) * self.cell_size
        x_center = x + self.cell_size // 2
        y_center = y + self.cell_size // 2

        if player == "X":
            self.canvas.create_line(x + 15, y + 15, x + self.cell_size - 15, y + self.cell_size - 15, width=self.line_width, fill="", outline="blue", capstyle=tk.ROUND)
            self.canvas.create_line(x + self.cell_size - 15, y + 15, x + 15, y + self.cell_size - 15, width=self.line_width, fill="", outline="blue", capstyle=tk.ROUND)
        else:  # Player O
            self.canvas.create_oval(x + 15, y + 15, x + self.cell_size - 15, y + self.cell_size - 15, width=self.line_width, outline="red", fill="", capstyle=tk.ROUND)

    def check_win(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != ""):
                return True
        return False

    def check_draw(self):
        return all(square != "" for square in self.board)

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()