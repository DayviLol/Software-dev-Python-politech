import csv, json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, encoding='UTF-8') as inp:
        text = list(csv.DictReader(inp))

        with open(OUTPUT_FILENAME, 'w', encoding='UTF-8') as out:
            json.dump(text, out, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
