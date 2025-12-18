from hobbies_and_political.overall_fuzzy import evaluate_match

# Crisp definitions
def crisp_level(x: float) -> str:
    return "HIGH" if x >= 0.66 else "LOW"

def crisp_match(pol: float, hob: float) -> bool:
    return crisp_level(pol) == "HIGH" and crisp_level(hob) == "HIGH"

# Fuzzy decision
def fuzzy_match(pol: float, hob: float, threshold: float = 0.66) -> bool:
    return evaluate_match(pol, hob) >= threshold

def run():
    # Named example users (reusing your real test names)
    examples = [
        ("Isabelle", 0.80, 0.83),   # high–high
        ("Valentin", 0.80, 0.24),   # high–low
        ("Hans",     0.23, 0.77),   # low–high
        ("Lisa",     0.50, 0.80),   # medium–high
        ("Marc",     0.50, 0.50),   # medium–medium

        # Additional realistic users
        ("Sophie",   0.78, 0.52),   # high–medium
        ("Daniel",   0.65, 0.68),   # borderline–borderline
    ]

    print("USER\t\tPOL\tHOB\tFUZZY\tFUZZY_MATCH\tCRISP_MATCH")
    print("-" * 75)

    fuzzy_count = 0
    crisp_count = 0

    for name, p, h in examples:
        f = evaluate_match(p, h)
        f_match = fuzzy_match(p, h)
        c_match = crisp_match(p, h)

        fuzzy_count += int(f_match)
        crisp_count += int(c_match)

        print(f"{name:10}\t{p:.2f}\t{h:.2f}\t{f:.3f}\t{str(f_match):10}\t{str(c_match)}")

    print("-" * 75)
    print(f"Total fuzzy matches: {fuzzy_count}/{len(examples)}")
    print(f"Total crisp matches: {crisp_count}/{len(examples)}")

if __name__ == "__main__":
    run()
