# This program is a quiz game about books and their authors.
#This program was written by Kübra Yeşilkaya and Ece Polat for the project assignment of the Python Programming course.

from tkinter import * # to build a GUI application using Tkinter
from tkinter import messagebox # messagebox module to show the score at the end of the game
import json

class Game:
    def __init__(self):
        self.question_number = 0
        self.display_title()
        self.display_question()
        self.selected_option = IntVar() # selected_option holds an integer value for selected option in a question
        self.options = self.radio_buttons() # view options for the question with radio buttons
        self.display_options()
        self.buttons() # button for the next and exit
        self.number_of_questions = len(question)
        self.correct_answer_numbers = 0

    # this method counts the number of correct and wrong answers, and at the end, displays them as a message Box
    def display_result(self):

        # we subtract the number of correct questions from
        # the total number of questions and find the number of wrong questions.
        wrong_answer_numbers = self.number_of_questions - self.correct_answer_numbers
        correctNumber = f"Correct: {self.correct_answer_numbers}"
        TotalWrong = f"Wrong: {wrong_answer_numbers}"

        # here we calculates score
        score = int(self.correct_answer_numbers / self.number_of_questions * 100)
        result = f"Score: {score}%"

        #  we print text according to success status.
        if score == 100:
            successStatus = "You are wonderful."
        elif score > 60:
            successStatus = "Too soon to succeed."
        elif score > 30:
            successStatus = "Don't give up, you can."
        else:
            successStatus = "You need to learn more."

        # we show a message box to display the result.
        messagebox.showinfo("Result", f"{result}\n{correctNumber}\n{TotalWrong}\n{successStatus}")

    def check_answer(self, question_number):
        # checks for if the selected option is correct
        if self.selected_option.get() == answer[question_number]:
            return True

    def nextButton(self):

        # If checks our answer and accordingly increases our number of true and false.
        if self.check_answer(self.question_number):
            # if the answer is correct it increments the correct_answer_numbers 1
            self.correct_answer_numbers += 1

        # Moves on to the next question
        self.question_number += 1

        # If the question is finished, we print the result on the screen and destroy the window.
        if self.question_number == self.number_of_questions:
            self.display_result()
            window.destroy()
        else:
            # shows the next question
            self.display_question()
            self.display_options()


    def buttons(self):
        # This method shows the two buttons on the screen.
        # The next_Btn moves to next question
        # logoutBtn closes the GUI window without completing the game.

        # progress button
        nextBtn = Button(window, text="Next", width=10, bg="purple", fg="white", font=("Helvetica", 18, "bold"),
                         command=self.nextButton)
        nextBtn.place(x=500, y=500)

        # logout button
        logoutBtn = Button(window, text="Logout", width=8, bg="purple", fg="white", font=("Helvetica", 18, " bold"),
                           command=window.destroy)
        logoutBtn.place(x=950, y=100)

    def display_options(self):
        value  = 0

        # we remove the previous selection
        self.selected_option.set(0)

        # we use a loop so that we can see the options for each question
        for option in options[self.question_number]:
            self.options[value]['text'] = option
            value += 1

    def display_question(self):
        # In this method, we pull the questions from the json file and
        # give them to the screen.

        question_number = Label(window, text=question[self.question_number], width=200,
                     font=('Helvetica', 14, 'bold'), anchor='w')

        # we indicate its position on the screen.
        question_number.place(x=50, y=220)

    def display_title(self):

        # we set the title of our game and

        title = Label(window, text="Books Informations Game",
                      width=71, bg="purple", fg="white", font=("ariel", 20, "bold"))

        # set its position on the screen.
        title.place(x=0, y=2)

    def radio_buttons(self):

        # we create an empty list.
        list = []

        # we determine the position of the first option
        position_Y = 300

        # we add the options to the list with the while loop.
        while len(list) < 4:

            radioButton = Radiobutton(window, text=" ", variable=self.selected_option,
                                    value=len(list)+1, font=("ariel", 20))

            # we add the buttons to the list that we created, with the append method.
            list.append(radioButton)

            # button position
            radioButton.place(x=60, y=position_Y)

            # we determine the position of the other options over the first option.
            position_Y += 40

        # return the radio buttons
        return list


# we are creating an object named window from the Tk() class.
window = Tk()

# we adjust the size of the window to open.
window.geometry("1200x700")

# we set the title of the window (Quiz Game)
window.title("Books Informations Game")

# we get the data from the json file where we store our data.
with open('informations.json') as f:
    info = json.load(f)

# we send the questions,options and answers in the file to the variables.
question = (info['question'])
options = (info['options'])
answer = (info['answer'])

# we create an object of the Game Class.
game = Game()

# we add it so that our code runs in an unlimited loop.
window.mainloop()

