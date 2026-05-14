from flask import Flask, render_template, request
from functions import countdown, score_result

app = Flask(__name__)

@app.route('/')
def show_intro():
    days_before_summer = countdown()
    return render_template('intro.html', days_before_summer=days_before_summer)

@app.route('/manifesto')
def show_manifesto():
    return render_template('manifesto.html')

@app.route('/checkin', methods=["GET", "POST"])
def show_checkin():
    if request.method == "GET":
        return render_template('checkin.html')
    else:
        answers = {}
        for category in request.form:
            answers[category] = (request.form[category])
        results = score_result(answers)
        return render_template('result.html', results=results)





if __name__ == "__main__":
    app.run()

