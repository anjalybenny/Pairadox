# pairadox_full.py
from evaluation_fuzzy import evaluate_match

from questions import QUESTIONS_DATA
from fuzzy_matching_pol import FuzzyMatcher

from hobby_questionnaire import get_hobby_answers_from_user
from hobby_control_system import map_tuple_to_fuzzy_inputs, compute_hobby_categories
from hobby_matching_system import compute_compatibility_from_profiles


# ---------- POLITICAL PART ----------

def get_political_answers_from_user(name: str):
    """
    Ask one user all political questions and return a tuple of floats (0–1).
    Uses the same questions as Anjaly's main.py.
    """
    print(f"\n=== Political Questionnaire for {name} ===")
    print("Please answer each question on a scale of [0.0 to 1.0]")
    print("0.0 = Agrees with LEFT statement")
    print("1.0 = Agrees with RIGHT statement")
    print("-" * 60)

    answers = []

    for i, q in enumerate(QUESTIONS_DATA, start=1):
        print(f"\nQ{i}: {q['question']}")
        print(f"   [0.0]: {q['left']}")
        print(f"   [1.0]: {q['right']}")

        while True:
            val = input("Your Score (0.0 - 1.0): ")
            try:
                num = float(val)
                if 0.0 <= num <= 1.0:
                    answers.append(num)
                    break
                else:
                    print(">>> Please enter a value between 0.0 and 1.0.")
            except ValueError:
                print(">>> Invalid input. Please enter a number like 0.3 or 0.75.")

    return tuple(answers)


def compute_political_total_diff(a_answers, b_answers) -> float:
    """
    Sum of absolute differences between two users' political answers.
    """
    return sum(abs(a - b) for a, b in zip(a_answers, b_answers))


def compute_political_compatibility(diff: float) -> float:
    """
    Use Anjaly's FuzzyMatcher to turn the total difference into
    a single compatibility score between 0 and 1.
    """
    matcher = FuzzyMatcher()

    # This assumes get_fuzzy_match_level(diff) returns a dict-like object
    # with keys 'low', 'medium', 'high'.
    levels = matcher.get_fuzzy_match_level(diff)

    low = float(levels.get("low", 0.0))
    med = float(levels.get("medium", 0.0))
    high = float(levels.get("high", 0.0))

    total = low + med + high
    if total == 0:
        return 0.0

    # Map: low -> 0.0, medium -> 0.5, high -> 1.0
    compat = (0.0 * low + 0.5 * med + 1.0 * high) / total
    return compat


# ---------- HOBBY PART ----------

def compute_hobby_profile_from_answers(raw_answers):
    """
    Take the 24 hobby answers (tuple of 0–1 values),
    map them to fuzzy inputs and compute the 9-category hobby profile.
    """
    fuzzy_input = map_tuple_to_fuzzy_inputs(raw_answers)
    profile = compute_hobby_categories(fuzzy_input)
    return profile


# ---------- MAIN FULL MATCH ----------

def main():
    print("=== Pairadox: Political + Hobby Matching ===")

    # You can change these names if you want (for example: 'Isabelle' and 'Valentin')
    name_a = "Isabelle"
    name_b = "Valentin"

    # ----- Isabelle -----
    print("\n############################")
    print(f"### {name_a}: ANSWERS ###")
    print("############################")

    pol_a = get_political_answers_from_user(name_a)
    hobby_raw_a = get_hobby_answers_from_user()
    hobby_profile_a = compute_hobby_profile_from_answers(hobby_raw_a)

    # ----- Valentin
    #  -----
    print("\n############################")
    print(f"### {name_b}: ANSWERS ###")
    print("############################")

    pol_b = get_political_answers_from_user(name_b)
    hobby_raw_b = get_hobby_answers_from_user()
    hobby_profile_b = compute_hobby_profile_from_answers(hobby_raw_b)

     # ----- POLITICAL MATCH -----
    pol_diff = compute_political_total_diff(pol_a, pol_b)
    pol_compat = compute_political_compatibility(pol_diff)

    # ----- HOBBY MATCH -----
    hobby_diff, hobby_compat = compute_compatibility_from_profiles(
        hobby_profile_a, hobby_profile_b
    )

    # ----- OVERALL EVALUATION -----
    overall = evaluate_match(pol_compat, hobby_compat)

    if overall < 0.33:
        overall_label = "LOW"
    elif overall < 0.66:
        overall_label = "MEDIUM"
    else:
        overall_label = "HIGH"

    # ----- DISPLAY RESULTS -----
    print("\n==================== MATCH RESULTS ====================")
    print(f"Political total difference:     {pol_diff:.3f}")
    print(f"Political compatibility (0–1):  {pol_compat:.3f}")
    print(f"Hobby total difference:         {hobby_diff:.3f}")
    print(f"Hobby compatibility (0–1):      {hobby_compat:.3f}")
    print("-------------------------------------------------------")
    print(f"Overall match (0–1):            {overall:.3f}")
    print(f"Final fuzzy label:              {overall_label}")
    print("=======================================================")


if __name__ == "__main__":
    main()
