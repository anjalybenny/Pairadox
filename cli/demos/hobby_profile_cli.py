from hobbies.questionnaire import get_hobby_answers_from_user
from hobbies.control_system import map_tuple_to_fuzzy_inputs, compute_hobby_categories

def main():

    raw_answers = get_hobby_answers_from_user()
    user_inputs = map_tuple_to_fuzzy_inputs(raw_answers)
    scores = compute_hobby_categories(user_inputs)
    print("\n=== Your Hobby Profile ===")
    for category, value in scores.items():
        print(f"{category}: {value:.3f}")

if __name__ == "__main__":
    main()
