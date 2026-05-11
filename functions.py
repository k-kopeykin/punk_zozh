from datetime import date


def countdown():
    current_day = date.today()
    summer_starts = date(2026, 6, 1)
    summer_starts_in = summer_starts - current_day

    return summer_starts_in.days

countdown()