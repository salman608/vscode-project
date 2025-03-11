import json
import tkinter as tk
from tkinter import messagebox

# Leaderboard File
LEADERBOARD_FILE = "leaderboard.json"

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")

        self.category = None
        self.current_question = 0
        self.score = 0
        self.questions = []
        self.username = ""

        self.load_categories()
        self.load_leaderboard()

        # Username Input
        self.username_label = tk.Label(self.root, text="Enter your name:", font=("Arial", 14))
        self.username_label.pack()

        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()

        self.start_button = tk.Button(self.root, text="Start Quiz", command=self.get_username)
        self.start_button.pack()

    def get_username(self):
        """Get username and show category selection"""
        self.username = self.username_entry.get().strip()
        if not self.username:
            messagebox.showwarning("Warning", "Please enter your name!")
            return

        self.show_category_selection()

    def show_category_selection(self):
        """Show category selection menu"""
        self.username_label.pack_forget()
        self.username_entry.pack_forget()
        self.start_button.pack_forget()

        self.category_label = tk.Label(self.root, text="Select a category:", font=("Arial", 14))
        self.category_label.pack()

        self.category_var = tk.StringVar()
        self.category_menu = tk.OptionMenu(self.root, self.category_var, *self.categories, command=self.load_questions)
        self.category_menu.pack()

    def load_categories(self):
        """Load available categories from questions.json"""
        try:
            with open("questions.json", "r") as file:
                self.all_questions = json.load(file)
                self.categories = list(self.all_questions.keys())
        except (FileNotFoundError, json.JSONDecodeError):
            messagebox.showerror("Error", "Error loading categories from questions.json!")
            self.categories = []

    def load_questions(self, selected_category):
        """Load questions for the selected category"""
        self.category = selected_category
        self.questions = self.all_questions.get(selected_category, [])
        self.current_question = 0
        self.score = 0

        if not self.questions:
            messagebox.showerror("Error", f"No questions found for {selected_category}!")
        else:
            self.show_quiz_ui()
            self.display_question()

    def show_quiz_ui(self):
        """Set up quiz UI"""
        self.category_label.pack_forget()
        self.category_menu.pack_forget()

        # Question Label
        self.question_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.question_label.pack()

        # Options
        self.options_var = tk.IntVar()
        self.options_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(self.root, text="", variable=self.options_var, value=i)
            btn.pack()
            self.options_buttons.append(btn)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.submit_button.pack()

    def display_question(self):
        """Display the current question and options"""
        if self.current_question < len(self.questions):
            q = self.questions[self.current_question]
            self.question_label.config(text=q["question"])

            for i, option in enumerate(q["options"]):
                self.options_buttons[i].config(text=option)

            self.options_var.set(-1)
        else:
            self.show_result()

    def check_answer(self):
        """Check the user's answer and move to the next question"""
        selected = self.options_var.get()
        if selected == -1:
            messagebox.showwarning("Warning", "Please select an answer")
            return

        correct_answer = self.questions[self.current_question]["answer"]
        if selected == correct_answer:
            self.score += 1

        self.current_question += 1
        self.display_question()

    def show_result(self):
        """Display the final score and update leaderboard"""
        messagebox.showinfo("Quiz Complete", f"Your score: {self.score}/{len(self.questions)}")
        self.update_leaderboard()
        self.show_leaderboard()

    def load_leaderboard(self):
        """Load leaderboard from JSON file"""
        try:
            with open(LEADERBOARD_FILE, "r") as file:
                self.leaderboard = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.leaderboard = {}

    def update_leaderboard(self):
        """Update leaderboard with the latest score"""
        if self.username in self.leaderboard:
            self.leaderboard[self.username] = max(self.score, self.leaderboard[self.username])
        else:
            self.leaderboard[self.username] = self.score

        with open(LEADERBOARD_FILE, "w") as file:
            json.dump(self.leaderboard, file, indent=4)

    def show_leaderboard(self):
        """Display the leaderboard"""
        leaderboard_text = "\n".join([f"{user}: {score}" for user, score in sorted(self.leaderboard.items(), key=lambda x: x[1], reverse=True)])
        messagebox.showinfo("Leaderboard", f"Top Scores:\n{leaderboard_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()


  