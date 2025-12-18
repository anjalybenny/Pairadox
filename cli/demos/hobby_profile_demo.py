
from hobbies.control_system import (
    map_tuple_to_fuzzy_inputs,
    compute_hobby_categories,
)
DEMO_USERS = [
    {
        "name": "Marc",
        "hobby_answers": (
            0.6, 0.6, 0.3, 0.6,
            0.6, 0.6, 0.6,
            0.6, 0.6, 0.6, 0.6,
            0.6, 0.6, 0.6,
            0.6, 0.6,
            0.6, 0.3,
            0.3,
            0.6, 0.6,
            0.6, 0.6, 0.6,
        ),
    },
    {
        "name": "Lisa",
        "hobby_answers": (
            0.9, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1,
            0.1, 0.1, 0.1, 0.1,
            0.1, 0.1, 0.1,
            0.1, 0.1,
            0.1, 0.1,
            0.1,
            0.1, 0.1,
            0.1, 0.1, 0.1,
        ),
    },
]


def main():
    print("\n Hobby Fuzzy Profile Demo \n")

    for user in DEMO_USERS:
        fuzzy_inputs = map_tuple_to_fuzzy_inputs(user["hobby_answers"])
        profile = compute_hobby_categories(fuzzy_inputs)

        print(f"User: {user['name']}")
        for category, value in profile.items():
            print(f"  {category:<22}: {value:.2f}")
        print("-" * 45)

if __name__ == "__main__":
    main()
