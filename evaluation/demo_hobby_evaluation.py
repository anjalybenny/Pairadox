from itertools import combinations
from hobbies.control_system import map_tuple_to_fuzzy_inputs
from evaluation.compare_models_hobby import compare_fuzzy_vs_crisp


USERS = [
    {
        "name": "Alice (Arts & Wellness)",
        "hobbies": (
            0.2, 0.2, 0.2, 0.2,      # Outdoors
            0.2, 0.2, 0.2,           # Sports & Fitness
            0.9, 0.9, 0.9, 0.9,      # Arts & Culture
            0.3, 0.3, 0.3,           # Social & Lifestyle
            0.3, 0.3,                # Travel & Discovery
            0.2, 0.2,                # Tech & Entertainment
            0.2,                     # Creative & DIY
            0.2, 0.2,                # Learning & Growth
            0.9, 0.9, 0.9,           # Wellness & Mindfulness
        ),
    },
    {
        "name": "Bob (Arts & Wellness, weaker)",
        "hobbies": (
            # Outdoors (hiking, cycling, skiing, gardening)
            0.2, 0.2, 0.2, 0.2,

            # Sports & Fitness (walking, fitness, swimming)
            0.2, 0.2, 0.2,

            # Arts & Culture (music, reading, films/series, photography)
            0.6, 0.6, 0.6, 0.6,

            # Social & Lifestyle (cooking, eating out, volunteering)
            0.3, 0.3, 0.3,

            # Travel & Discovery (Switzerland, abroad)
            0.3, 0.3,

            # Tech & Entertainment (social media, video games)
            0.2, 0.2,

            # Creative & DIY (crafting)
            0.2,

            # Learning & Growth (languages, continuing education)
            0.2, 0.2,

            # Wellness & Mindfulness (meditation, yoga, spa/sauna)
            0.6, 0.6, 0.6,
        ),
    },
    {
        "name": "Clara (Outdoors & Sports)",
        "hobbies": (
            0.9, 0.9, 0.9, 0.9,
            0.9, 0.9, 0.9,
            0.2, 0.2, 0.2, 0.2,
            0.3, 0.3, 0.3,
            0.6, 0.6,
            0.3, 0.3,
            0.3,
            0.3, 0.3,
            0.2, 0.2, 0.2,
        ),
    },
    {
        "name": "Dan (Tech & Gaming)",
        "hobbies": (
            # Outdoors (hiking, cycling, skiing, gardening)
            0.3, 0.3, 0.3, 0.3,

            # Sports & Fitness (walking, fitness, swimming)
            0.3, 0.3, 0.3,

            # Arts & Culture (music, reading, films/series, photography)
            0.3, 0.3, 0.3, 0.3,

            # Social & Lifestyle (cooking, eating out, volunteering)
            0.3, 0.3, 0.3,

            # Travel & Discovery (Switzerland, abroad)
            0.3, 0.3,

            # Tech & Entertainment (social media, video games)
            0.9, 0.9,

            # Creative & DIY (crafting)
            0.3,

            # Learning & Growth (languages, continuing education)
            0.3, 0.3,

            # Wellness & Mindfulness (meditation, yoga, spa/sauna)
            0.3, 0.3, 0.3,
        ),
    },
]


def user_demo():
    print("\n Hobby compatibility (Fuzzy vs Crisp)\n")

    for u1, u2 in combinations(USERS, 2):
        ua = map_tuple_to_fuzzy_inputs(u1["hobbies"])
        ub = map_tuple_to_fuzzy_inputs(u2["hobbies"])

        result = compare_fuzzy_vs_crisp(ua, ub)

        print(f"{u1['name']} ↔ {u2['name']}")
        print(f"  Fuzzy : {result['fuzzy_compatibility']:.3f}")
        print(f"  Crisp : {result['crisp_compatibility']:.3f}")
        print()


if __name__ == "__main__":
    user_demo()
