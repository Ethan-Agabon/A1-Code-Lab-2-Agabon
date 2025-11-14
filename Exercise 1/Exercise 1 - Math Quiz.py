import tkinter as tk
import random
from tkinter import messagebox

def displayMenu():
    menu_frame.pack()
    quiz_frame.pack_forget()
    result_frame.pack_forget()


def randomInt(level):
    if level == "Easy":
        return random.randint(1, 9)
    elif level == "Moderate":
        return random.randint(10, 99)
    elif level == "Advanced":
        return random.randint(1000, 9999)


def decideOperation():
    return random.choice(["+", "-"])


def displayProblem():
    global num1, num2, operation, attempt
    attempt = 1

    num1 = randomInt(difficulty.get())
    num2 = randomInt(difficulty.get())
    operation = decideOperation()

    question_label.config(text=f"{num1} {operation} {num2} = ?")
    answer_entry.delete(0, tk.END)


def isCorrect():
    global score, questions_answered, attempt
    try:
        user_answer = int(answer_entry.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")
        return

    correct_answer = num1 + num2 if operation == "+" else num1 - num2

    if user_answer == correct_answer:
        if attempt == 1:
            score += 10
        else:
            score += 5
        feedback_label.config(text="Correct!", fg="green")
        questions_answered += 1

        if questions_answered < 10:
            displayProblem()
        else:
            displayResults()
    else:
        if attempt == 1:
            feedback_label.config(text="Incorrect, try again!", fg="red")
            attempt = 2
            answer_entry.delete(0, tk.END)
        else:
            feedback_label.config(text=f"Wrong again! Correct answer was {correct_answer}", fg="red")
            questions_answered += 1
            if questions_answered < 10:
                displayProblem()
            else:
                displayResults()


def displayResults():
    quiz_frame.pack_forget()
    result_frame.pack()

    grade = ""
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"

    result_label.config(text=f"Final Score: {score}/100\nGrade: {grade}")

root = tk.Tk()
root.title("Arithmetic Quiz")
root.geometry("400x300")

score = 0
questions_answered = 0
attempt = 1
num1 = num2 = 0
operation = ""

difficulty = tk.StringVar(value="Easy")

menu_frame = tk.Frame(root)
menu_title = tk.Label(menu_frame, text="DIFFICULTY LEVEL", font=("Arial", 16))
menu_title.pack(pady=10)

for level in ["Easy", "Moderate", "Advanced"]:
    rb = tk.Radiobutton(menu_frame, text=level, variable=difficulty, value=level)
    rb.pack(anchor="w")

def startQuiz():
    global score, questions_answered
    score = 0
    questions_answered = 0
    feedback_label.config(text="")

    menu_frame.pack_forget()
    quiz_frame.pack()
    displayProblem()

start_button = tk.Button(menu_frame, text="Start Quiz", command=startQuiz)
start_button.pack(pady=15)

quiz_frame = tk.Frame(root)
question_label = tk.Label(quiz_frame, text="", font=("Arial", 20))
question_label.pack(pady=20)

answer_entry = tk.Entry(quiz_frame, font=("Arial", 16))
answer_entry.pack()

submit_button = tk.Button(quiz_frame, text="Submit", command=isCorrect)
submit_button.pack(pady=10)

feedback_label = tk.Label(quiz_frame, text="", font=("Arial", 12))
feedback_label.pack()

result_frame = tk.Frame(root)
result_label = tk.Label(result_frame, text="", font=("Arial", 16))
result_label.pack(pady=20)


def playAgain():
    displayMenu()

again_button = tk.Button(result_frame, text="Play Again", command=playAgain)
again_button.pack(pady=10)

displayMenu()

root.mainloop()
