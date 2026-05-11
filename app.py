from flask import Flask, render_template
from functions import countdown

app = Flask(__name__)

@app.route('/')
def show_index():
    days_before_summer = countdown()
    return render_template('index.html', days_before_summer=days_before_summer)

@app.route('/manifesto')
def show_manifesto():
    return render_template('manifesto.html')

@app.route('/checkin')
def show_checkin():
    return render_template('checkin.html')


if __name__ == "__main__":
    app.run()

