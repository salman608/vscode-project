import tkinter as tk

# Create main window
window = tk.Tk()



class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("500x400")

        self.load_questions()
        self.current_question = 0
        self.score = 0
        
        self.question_label = tk.Label(root, text="", wraplength=400, font=("Arial", 12))
        self.question_label.pack(pady=20)
        
        self.options_var = tk.StringVar()
        self.options_buttons = []
        
        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.options_var, value=i, font=("Arial", 10))
            btn.pack(anchor="w")
            self.options_buttons.append(btn)
        
        self.submit_button = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 12))
        self.submit_button.pack(pady=20)
        
        self.quit_button = tk.Button(root, text="Quit", command=root.quit, font=("Arial", 12))
        self.quit_button.pack()
        
        self.display_question()
    
    def load_questions(self):
        with open("questions.json", "r") as file:
            self.questions = json.load(file)
    
    def display_question(self):
        question_data = self.questions[self.current_question]
        self.question_label.config(text=question_data["question"])
        
        for i, option in enumerate(question_data["options"]):
            self.options_buttons[i].config(text=option, value=option)
        
        self.options_var.set(None)
    
    def check_answer(self):
        selected_answer = self.options_var.get()
        if not selected_answer:
            messagebox.showwarning("Warning", "Please select an answer!")
            return
        
        correct_answer = self.questions[self.current_question]["answer"]
        if selected_answer == correct_answer:
            self.score += 1
        
        self.current_question += 1
        if self.current_question < len(self.questions):
            self.display_question()
        else:
            self.show_result()
    
    def show_result(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(self.questions)}")
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()







[
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "answer": "Mars"
    }
]
