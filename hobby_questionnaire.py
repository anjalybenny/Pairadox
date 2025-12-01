from hobby_questions import HOBBY_QUESTIONS_DATA


def get_hobby_answers_from_user():
    """
    Ask the user all hobby questions and return a tuple of floats (0–1).
    """
    print("\n--- Hobby Questionnaire ---")
    print("Please answer each question on a scale from 0.0 to 1.0")
    print("0.0 = you hate it")
    print("1.0 = you love it")
    print("-" * 60)

    answers = []

    for i, item in enumerate(HOBBY_QUESTIONS_DATA, start=1):
        print(f"\nQ{i}: {item['question_text']}")
        print(f"   Category: {item['category']}")
        print(f"   Hobby: {item['hobby']}")

        while True:
            val = input("Your answer (0.0 – 1.0): ")
            try:
                num = float(val)
                if 0.0 <= num <= 1.0:
                    answers.append(num)
                    break
                else:
                    print(">>> Enter a value between 0.0 and 1.0")
            except ValueError:
                print(">>> Not a number. Try again.")

    return tuple(answers)


if __name__ == "__main__":
    ans = get_hobby_answers_from_user()
    print("\nCollected hobby answers:")
    print(ans)
