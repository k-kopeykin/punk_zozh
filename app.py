from flask import Flask, render_template
from functions import countdown

app = Flask(__name__)

@app.route('/')
def show_intro():
    days_before_summer = countdown()
    return render_template('intro.html', days_before_summer=days_before_summer)

@app.route('/manifesto')
def show_manifesto():
    return render_template('manifesto.html')

@app.route('/checkin')
def show_checkin():
    return render_template('checkin.html')

@app.route('/result')
def show_result():
    return render_template('result.html')


if __name__ == "__main__":
    app.run()

