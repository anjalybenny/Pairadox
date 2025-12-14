"""
Crisp baseline model for hobby categories.
Uses simple linear averaging (no fuzzy logic).
"""

CRISP_CATEGORY_MAP = {
    "outdoors": ["hiking", "cycling", "skiing", "gardening"],
    "sports_fitness": ["walking", "fitness", "swimming"],
    "arts_culture": [
        "listening_music", "reading",
        "watching_films_or_series", "photography"
    ],
    "social_lifestyle": ["cooking", "eating_out", "volunteering"],
    "travel_discovery": ["travel_switzerland", "travel_abroad"],
    "tech_entertainment": ["social_media", "video_games"],
    "creative_diy": ["crafting_diy"],
    "learning_growth": ["learning_languages", "continuing_education"],
    "wellness_mindfulness": ["meditation", "yoga", "spa_sauna"],
}


def compute_hobby_categories_crisp(user: dict) -> dict:
    """
    Compute category scores by averaging hobby inputs.
    """
    return {
        category: sum(user[h] for h in hobbies) / len(hobbies)
        for category, hobbies in CRISP_CATEGORY_MAP.items()
    }
