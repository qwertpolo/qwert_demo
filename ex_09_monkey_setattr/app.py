import random
import datetime


def roll_3d6():
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    print(random.randint(1, 6))


def is_day_or_night():
    current_hour = datetime.datetime.now().hour

    if 6 <= current_hour < 18:
        return "Dzień"
    else:
        return "Noc"
