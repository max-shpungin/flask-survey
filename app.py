from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
#app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

responses = [] #todo

# When the user goes to the root route,
#     render a page that shows the user the title of the survey,
#     the instructions, and a button to start the survey.

#     The button should serve as a link that directs the user to
#     /questions/0 (the next step will define that route).

@app.get("/")
def show_survey_instructions():
    """Shows the initial survey page and start button"""

    return render_template("survey_start.html")

#^ /begin route is where the form goes so we should handle that


@app.post("/begin")
def handle_survey_start():
    """display the survey questions"""

    return redirect('/questions/0')


#need to handle the post request and turn it into a get... probably
#it should handle URLs like /questions/0 (the first question),
# /questions/1, and so on.


@app.get("/questions/<int:question_number>")
def display_question(question_number):

    question = survey.questions[question_number]

    #breakpoint()

    return render_template('question.html',
                    question = question,
                    question_number = question_number)


@app.post("/answer")
def handle_answer():
    """ Appends answer to responses list
        Redirects to next question
    """

    responses.append(request.form['answer'])


