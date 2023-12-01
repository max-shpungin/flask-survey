from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

#responses = []

@app.get("/")
def show_survey_instructions():
    """Shows the initial survey page and start button"""

    return render_template("survey_start.html",
                           survey = survey)


@app.post("/begin")
def handle_survey_start():
    """ Display the survey questions. """

    #responses.clear()

    return redirect('/questions/0')


@app.get("/questions/<int:question_number>")
def display_question(question_number):
    """ Display a specific question in the survey. """

    question = survey.questions[question_number]
    session['responses'] = session.get('responses', []) #if session. else []
    return render_template(
                    'question.html',
                    question = question,
                    question_number = question_number
    )


@app.post("/answer")
def handle_answer():
    """ Appends answer to responses list
        Redirects to next question. """

    # responses.append(request.form['answer'])

    responses = session['responses'] #if session['responses'] else []
   # breakpoint()

    responses.append(request.form['answer'])
    session['responses'] = responses

   # breakpoint()

    question_number = len(responses)

    if len(survey.questions) == question_number:
        return redirect('/ok-thanks')

    return redirect(f'/questions/{question_number}')

@app.get("/ok-thanks")
def thank_the_user():
    """ Thank the user for their valuable participation in our
        survey."""

    responses = session['responses']

    return render_template('completion.html',
                           responses = responses,
                           questions = survey.questions)


# What if they just manually type in questions/2 ? Needs an error.
# What if, what if?
# jinja 8M+ dl's wholroyd for syntax highlighting? TODO: look into this.