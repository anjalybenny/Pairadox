from evaluation_fuzzy import evaluate_match

def label(score: float) -> str:
    if score < 0.33:
        return "LOW"
    elif score < 0.66:
        return "MEDIUM"
    return "HIGH"

def run_grid_test():
    levels = {"low": 0.2, "medium": 0.5, "high": 0.8}
    cases = [
        ("low", "low"), ("low", "medium"), ("low", "high"),
        ("medium", "low"), ("medium", "medium"), ("medium", "high"),
        ("high", "low"), ("high", "medium"), ("high", "high"),
    ]

    print("POL\tHOB\tFUZZY\tLBL\tBASELINE")
    print("-" * 50)

    for p_name, h_name in cases:
        p = levels[p_name]
        h = levels[h_name]

        fuzzy = evaluate_match(p, h)
        base = 0.5 * p + 0.5 * h

        print(f"{p_name:6}\t{h_name:6}\t{fuzzy:.3f}\t{label(fuzzy):6}\t{base:.3f}")

if __name__ == "__main__":
    run_grid_test()
