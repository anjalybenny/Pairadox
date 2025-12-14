from config.hobby_questions import HOBBY_QUESTIONS_DATA

def get_hobby_answers_from_user() -> tuple:
    answers = []

    for item in HOBBY_QUESTIONS_DATA:
        while True:
            try:
                v = float(input(f"{item['question_text']} (0–1): "))
                if 0.0 <= v <= 1.0:
                    answers.append(v)
                    break
            except ValueError:
                pass

    return tuple(answers)
