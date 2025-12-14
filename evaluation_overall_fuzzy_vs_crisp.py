from evaluation_fuzzy import evaluate_match

def crisp_level(x: float) -> str:
    return "HIGH" if x >= 0.66 else "LOW"

def crisp_match(pol: float, hob: float) -> str:
    return "MATCH" if (crisp_level(pol) == "HIGH" and crisp_level(hob) == "HIGH") else "NO MATCH"

def run():
    levels = {"low": 0.2, "medium": 0.5, "high": 0.8}
    cases = [
        ("low", "low"), ("low", "medium"), ("low", "high"),
        ("medium", "low"), ("medium", "medium"), ("medium", "high"),
        ("high", "low"), ("high", "medium"), ("high", "high"),
    ]

    print("POL\tHOB\tFUZZY\tFUZZY_LBL\tCRISP_DECISION")
    print("-" * 65)

    for p_name, h_name in cases:
        p = levels[p_name]
        h = levels[h_name]

        fuzzy = evaluate_match(p, h)
        fuzzy_lbl = "LOW" if fuzzy < 0.33 else ("MEDIUM" if fuzzy < 0.66 else "HIGH")
        crisp_decision = crisp_match(p, h)

        print(f"{p_name:6}\t{h_name:6}\t{fuzzy:.3f}\t{fuzzy_lbl:9}\t{crisp_decision}")

if __name__ == "__main__":
    run()
