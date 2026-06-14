from flask import Flask, render_template, request, session, redirect, flash
from functions import countdown, score_result, day_word, get_summer_phrase, micro_actions, today_or_yesterday

app = Flask(__name__)
app.secret_key = 'super_secret_punk_zozh_key_2026'

@app.route('/')
def show_home():
    saved_action = session.get('current_action')
    if not saved_action:
        days_before_summer = countdown()
        word = day_word(days_before_summer)
        summer_phrase = get_summer_phrase(days_before_summer)
        return render_template('intro.html', days_before_summer=days_before_summer, word=word, summer_phrase=summer_phrase)
    else:
        return render_template('home.html', action=saved_action)
    
@app.route('/manifesto')
def show_manifesto():
    return render_template('manifesto.html')

@app.route('/checkin', methods=["GET", "POST"])
def show_checkin():
    if request.method == "GET":
        return render_template('checkin.html')
    else:
        categories = ['food', 'sleep', 'emotion', 'activity']
        answers = {key: int(value) for key, value in request.form.items() if key in categories}
        if len(answers) < 4:
            flash("Заполни все 4 поля, герой. Организм сам себя не оценит.", "warning")
            return redirect('/checkin')
        else:
            results = score_result(answers)
            action = micro_actions(answers)
            session['current_action'] = action
            session['checkin_date'] = today_or_yesterday()
            return render_template('result.html', results=results, action=action)

@app.route('/acknowledge')
def acknowledged():
    status = request.args.get('status')
    session.pop('current_action', None)
    if status == 'done':
        flash("Организм оценил твои усилия. Красавчик!" , "success")
    else:
        flash("Принято. Едем дальше", "info")
    return redirect('/')

@app.route('/crisis')
def show_crisis():
    return render_template('crisis.html')

@app.route('/articles')
def show_articles():
    return render_template('articles.html')




if __name__ == "__main__":
    app.run()

