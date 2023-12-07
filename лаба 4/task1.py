import json


def task() -> float:
    with open('input.json') as file:
        text = json.load(file)

    list_of_mult = [d['score'] * d['weight'] for d in text]
    return round(sum(list_of_mult), 3)

print(task())
