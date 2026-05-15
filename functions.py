from datetime import date
import json
from random import choice

def score_result(answers):
    
    with open('texts.json', 'r', encoding='utf-8') as f:
        texts = json.load(f)
        result = []
        for category in answers:
            result.append(texts[category][answers[category]])
    return result



def countdown():
    current_day = date.today()
    summer_starts = date(2026, 6, 1)
    summer_starts_in = summer_starts - current_day
    summer_starts_in = summer_starts_in.days
    return summer_starts_in

def day_word(summer_starts_in):
    last_digit = summer_starts_in % 10
    last_two_digits = summer_starts_in % 100
    if last_digit == 1 and last_two_digits !=11:
        word = "день"
    elif 2 <= last_digit <= 4 and not (12 <= last_two_digits <= 14):
        word = "дня"
    else:
        word = "дней"
    return word

def get_summer_phrase(summer_starts_in):
    with open("summer_texts.json", "r", encoding="utf-8") as f:
        summer_phrases = json.load(f)
    if 1 <= summer_starts_in <= 21:
        summer_phrase = choice(summer_phrases["1-21"])
    elif 22 <= summer_starts_in <= 60:
        summer_phrase = choice(summer_phrases["22-60"])
    elif 61 <= summer_starts_in <= 120:
        summer_phrase = choice(summer_phrases["61-120"])
    elif 121 <= summer_starts_in <= 240:
        summer_phrase = choice(summer_phrases["121-240"])
    elif 241 <= summer_starts_in <= 365:
        summer_phrase = choice(summer_phrases["241-365"])
    else:
        summer_phrase = "Вот такое странное лето..."
    return summer_phrase
    


