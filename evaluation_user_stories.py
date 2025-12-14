from evaluation_fuzzy import evaluate_match

stories = [
    ("Similar politics + similar hobbies", 0.8, 0.8),
    ("Opposite politics + similar hobbies", 0.2, 0.8),
    ("Similar politics + opposite hobbies", 0.8, 0.2),
]

for name, p, h in stories:
    overall = evaluate_match(p, h)
    print(f"{name}: pol={p}, hobby={h} -> overall={overall:.3f}")
