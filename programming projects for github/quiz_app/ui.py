from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window =  Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg = THEME_COLOR)



    #score label
        self.score_label = Label(text='Score: 0', fg='white', bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
    #canvas
        self.canvas = Canvas(height=250, width= 300, bg='white')
        #canvas_text
        # canvas_text = canvas.create_text(125, 150, text='&quot;Typewriter&quot; is the longest word that can be typed using only the first row on a QWERTY keyboard')
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            text='Peter Molyneux was the founder of Bullfrog Productions.',
            width=280,
            font=('Ariel', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)


    #checkbutton
        # true_img = PhotoImage
        true_photo =PhotoImage(file='images/true.png')
        self.trueButton = Button(image=true_photo, highlightthickness=0, command=self.truepressed)
        self.trueButton.grid(column=0, row=2)
    #crossButton
        false_photo = PhotoImage(file='images/false.png')
        self.falseButton = Button(image=false_photo, highlightthickness=0, command=self.falsepressed)
        self.falseButton.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text='You have reached the end of the quiz.')
            self.trueButton.config(state='disabled')
            self.falseButton.config(state='disabled')

    def truepressed(self):
        self.give_feedback(self.quiz.check_answer('True'))
    def falsepressed(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
