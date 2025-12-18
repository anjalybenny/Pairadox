from hobbies.control_system import compute_hobby_categories
from evaluation.crisp_hobby_model import compute_hobby_categories_crisp


def compute_total_profile_difference(profile_a, profile_b):
    return sum(abs(profile_a[k] - profile_b[k]) for k in profile_a)


def compute_compatibility_from_profiles(profile_a, profile_b):
    diff = compute_total_profile_difference(profile_a, profile_b)
    max_diff = len(profile_a)
    compatibility = 1.0 - min(diff / max_diff, 1.0)
    return diff, compatibility


def compare_fuzzy_vs_crisp(user_a: dict, user_b: dict):
    fuzzy_a = compute_hobby_categories(user_a)
    fuzzy_b = compute_hobby_categories(user_b)

    crisp_a = compute_hobby_categories_crisp(user_a)
    crisp_b = compute_hobby_categories_crisp(user_b)

    _, fuzzy_compat = compute_compatibility_from_profiles(fuzzy_a, fuzzy_b)
    _, crisp_compat = compute_compatibility_from_profiles(crisp_a, crisp_b)

    return {
        "fuzzy_compatibility": fuzzy_compat,
        "crisp_compatibility": crisp_compat,
    }
