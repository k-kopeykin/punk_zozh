from datetime import date
import json


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

    return summer_starts_in.days

score = []
for i in range(4):
    score += str(i)
print(score)

