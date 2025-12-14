from hobbies.control_system import compute_hobby_categories
from evaluation.crisp_hobby_model import compute_hobby_categories_crisp
from hobbies.matching import compute_compatibility_from_profiles


def compare_fuzzy_vs_crisp(user_a: dict, user_b: dict):
    """
    Compare fuzzy and crisp hobby models using the same matching method.
    """

    # Fuzzy model category profiles
    fuzzy_a = compute_hobby_categories(user_a)
    fuzzy_b = compute_hobby_categories(user_b)
    _, fuzzy_compatibility = compute_compatibility_from_profiles(fuzzy_a, fuzzy_b)

    # Crisp model category profiles
    crisp_a = compute_hobby_categories_crisp(user_a)
    crisp_b = compute_hobby_categories_crisp(user_b)
    _, crisp_compatibility = compute_compatibility_from_profiles(crisp_a, crisp_b)

    return {
        "fuzzy_compatibility": fuzzy_compatibility,
        "crisp_compatibility": crisp_compatibility,
    }
