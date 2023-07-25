from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Create and format screen
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        # Create and format score:
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Create and format question:
        self.canvas = Canvas(width=300, height=250, bg="white")
        # Square format
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Some Question Text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Button picture True-False format
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        # Call next question
        self.get_next_question()

        # Mainloop screen update
        self.window.mainloop()

    # Search for the question in the next_question formula (in the quiz_brain sheet) and construct the following question
    def get_next_question(self):
        self.canvas.config(bg="white")                                  # New question format
        if self.quiz.still_has_questions():                             # If still have questions left, move on to the next question
            self.score_label.config(text=f"Score: {self.quiz.score}")   # To add the score with each correct answer
            q_text = self.quiz.next_question()                          # New questions text
            self.canvas.itemconfig(self.question_text, text=q_text)
        # If have no more questions, notify that it's the end and deactivate the buttons
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    # Function that runs with the true button. The check answer comes from quiz_brain
    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    # Function that runs with the false button
    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    # If it's correct, the background will turn green for one second, and if it's incorrect, the background will turn red
    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        # To delay for 1000 milliseconds with the color red or green and then call the new question
        self.window.after(1000, self.get_next_question)







