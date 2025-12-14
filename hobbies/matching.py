def compute_total_profile_difference(profile_a, profile_b):
    """
    Sum of absolute differences between two hobby profiles.
    """
    return sum(abs(profile_a[k] - profile_b[k]) for k in profile_a)


def compute_compatibility_from_profiles(profile_a, profile_b):
    """
    Low difference = high compatibility.
    Returns (difference, compatibility_score).
    """
    diff = compute_total_profile_difference(profile_a, profile_b)

    max_diff = len(profile_a)  # number of hobby categories (e.g. 9)
    compatibility = 1.0 - min(diff / max_diff, 1.0)

    return diff, compatibility
