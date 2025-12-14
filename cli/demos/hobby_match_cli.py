from hobbies.questionnaire import get_hobby_answers_from_user
from hobbies.control_system import (
    map_tuple_to_fuzzy_inputs,
    compute_hobby_categories,
)

from hobbies.matching import (
    compute_compatibility_from_profiles,
)


def compute_user_profile_from_answers(answers_tuple):
    fuzzy_input = map_tuple_to_fuzzy_inputs(answers_tuple)
    profile = compute_hobby_categories(fuzzy_input)
    return profile


if __name__ == "__main__":
    print("=== User 1 ===")
    answers_a = get_hobby_answers_from_user()
    profile_a = compute_user_profile_from_answers(answers_a)

    print("\n=== User 2 ===")
    answers_b = get_hobby_answers_from_user()
    profile_b = compute_user_profile_from_answers(answers_b)

    diff, compat = compute_compatibility_from_profiles(profile_a, profile_b)

    print("\n--- MATCH RESULT ---")
    print("Isabelle", profile_a)
    print("Valentin:", profile_b)
    print("Total category difference:", diff)
    print("Hobby Compatability (0–1):", compat)

