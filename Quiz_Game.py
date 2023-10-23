import tkinter as tk
from tkinter import messagebox

# Define quiz questions and answers
quiz_data =[
    {
        "question": "What is the capital of Canada?",
        "options": ["A) Toronto", "B) Montreal", "C)  Ottawa", "D) Vancouver"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        "answer": "B"
    },
    {
        "question": "What is 7 x 8?",
        "options": ["A) 54", "B) 60", "C) 48", "D) 56"],
        "answer": "D"
    },
    {
       "question": "What is 24 x 32?",
        "options": ["A) 453", "B) 232", "C) 897", "D) 768"],
        "answer": "D" 
    },
    {
       "question": "What is the capital of Australia?",
        "options": ["A) Brazil", "B) Brisbane", "C)  Canberra", "D) Hobart"],
        "answer": "C"
    }
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MCQ Quiz Game")

        self.current_question = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=10)

        self.option_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            self.option_buttons.append(button)
            button.pack()

        self.update_question()

    def update_question(self):
        if self.current_question < len(quiz_data):
            question = quiz_data[self.current_question]
            self.question_label.config(text=question["question"])
            for i in range(4):
                self.option_buttons[i].config(text=question["options"][i])
        else:
            self.show_score()

    def check_answer(self, selected_option):
        question = quiz_data[self.current_question]
        if question["answer"] == chr(ord("A") + selected_option):
            self.score += 1
        self.current_question += 1
        self.update_question()

    def show_score(self):
        score_text = f"You scored {self.score}/{len(quiz_data)}."
        messagebox.showinfo("Quiz Over", score_text)
        self.root.destroy()


if __name__ == '__main__':
    
    root = tk.Tk()

    app = QuizApp(root)

    root.mainloop()