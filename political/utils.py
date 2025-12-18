def calculate_total_difference(user_a_answers, user_b_answers):
    # Step 4: Calculate differences
    diffs = []
    for i in range(len(user_a_answers)):
        d = abs(user_a_answers[i] - user_b_answers[i])
        diffs.append(d)

    total_diff = sum(diffs)
    return total_diff