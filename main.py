import random
import numpy as np
from questions import QUESTIONS_DATA, SWISS_PARTIES
from fuzzy_matching import FuzzyMatcher

# --- MOCK DATA GENERATOR ---
# Since we now have 30 questions, we generate mock answers 
# to ensure the lists are the correct length.
def generate_mock_answers(bias):
    """
    bias: 'left' (favors 0.0-0.4), 'right' (favors 0.6-1.0), 'center' (favors 0.3-0.7)
    """
    answers = []
    for _ in range(30):
        if bias == 'left':
            val = random.uniform(0.0, 0.4)
        elif bias == 'right':
            val = random.uniform(0.6, 1.0)
        else:
            val = random.uniform(0.3, 0.7)
        answers.append(round(val, 2))
    return tuple(answers)

MOCK_USERS = [
    {"name": "Hans ", "answers": generate_mock_answers('right')},
    {"name": "Lisa ",  "answers": generate_mock_answers('left')},
    {"name": "Marc ",   "answers": generate_mock_answers('center')}
]

def get_user_input():
    print("\n--- User Input ---")
    print("Please answer the following questions on a scale of [0.0 to 1.0]")
    print("0.0 = Agrees with LEFT statement")
    print("1.0 = Agrees with RIGHT statement")
    print("-" * 60)
    
    user_answers = []
    
    for i, item in enumerate(QUESTIONS_DATA):
        print(f"\nQ{i+1}: {item['question']}")
        print(f"   [0.0]: {item['left']}")
        print(f"   [1.0]: {item['right']}")
        
        while True:
            try:
                val_str = input("Your Score (0.0 - 1.0): ")
                val = float(val_str)
                if 0.0 <= val <= 1.0:
                    user_answers.append(val)
                    break
                else:
                    print(">> Please enter a number between 0.0 and 1.0")
            except ValueError:
                print(">> Invalid input. Please enter a number (e.g., 0.5, 0.2).")
    
    return tuple(user_answers)

def calculate_total_difference(user_a_answers, user_b_answers):
    # Step 4: Calculate differences
    diffs = []
    for i in range(len(user_a_answers)):
        d = abs(user_a_answers[i] - user_b_answers[i])
        diffs.append(d)
    
    total_diff = sum(diffs)
    return total_diff



def main():
    # Initialize Fuzzy Logic System
    fuzzy_system = FuzzyMatcher()

    # 1. Get Inputs
    # Note: This will ask 30 questions. For quick testing, you might want to slice the list,
    # but strictly speaking, it needs all 30 for the math to hold up.
    my_answers = get_user_input()
    

    # 2. Compare with other users
    print("\n--- Matching with other users ---")
    print(f"{'Users':<25} | {'Diff':<10} | {'Low (Match)':<12} | {'Med (Match)':<12} | {'High (Match)':<12}")
    print("-" * 85)

    for other_user in MOCK_USERS:
        total_diff = calculate_total_difference(my_answers, other_user['answers'])
        match_levels = fuzzy_system.get_fuzzy_match_level(total_diff)
        
        print(f"{other_user['name']:<25} | {total_diff:<10.2f} | "
              f"{match_levels['low']:<12.2f} | {match_levels['medium']:<12.2f} | {match_levels['high']:<12.2f}")

    # Optional: Visualize
    # fuzzy_system.visualize()

if __name__ == "__main__":
    main()