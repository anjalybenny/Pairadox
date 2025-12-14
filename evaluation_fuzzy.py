import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Inputs: compatibility scores from 0 to 1
political_match = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'political_match')
hobby_match = ctrl.Antecedent(np.arange(0, 1.01, 0.01), 'hobby_match')

# Output: overall match 0–1
overall_match = ctrl.Consequent(np.arange(0, 1.01, 0.01), 'overall_match')

# Fuzzy sets for inputs
for var in (political_match, hobby_match):
    var['low'] = fuzz.trimf(var.universe, [0.0, 0.0, 0.5])
    var['medium'] = fuzz.trimf(var.universe, [0.25, 0.5, 0.75])
    var['high'] = fuzz.trimf(var.universe, [0.5, 1.0, 1.0])

# Fuzzy sets for output
overall_match['low'] = fuzz.trimf(overall_match.universe, [0.0, 0.0, 0.5])
overall_match['medium'] = fuzz.trimf(overall_match.universe, [0.25, 0.5, 0.75])
overall_match['high'] = fuzz.trimf(overall_match.universe, [0.5, 1.0, 1.0])

# Rules to combine political + hobby
rule1 = ctrl.Rule(political_match['high'] & hobby_match['high'], overall_match['high'])
rule2 = ctrl.Rule(political_match['high'] & hobby_match['medium'], overall_match['high'])
rule3 = ctrl.Rule(political_match['medium'] & hobby_match['high'], overall_match['high'])

rule4 = ctrl.Rule(political_match['medium'] & hobby_match['medium'], overall_match['medium'])
rule5 = ctrl.Rule(political_match['high'] & hobby_match['low'], overall_match['medium'])
rule6 = ctrl.Rule(political_match['low'] & hobby_match['high'], overall_match['medium'])

rule7 = ctrl.Rule(political_match['low'] & hobby_match['medium'], overall_match['low'])
rule8 = ctrl.Rule(political_match['medium'] & hobby_match['low'], overall_match['low'])
rule9 = ctrl.Rule(political_match['low'] & hobby_match['low'], overall_match['low'])

evaluation_ctrl = ctrl.ControlSystem(
    [rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9]
)

def evaluate_match(political_score: float, hobby_score: float) -> float:
    """
    Combine political and hobby compatibility (0–1 each)
    into an overall match score (0–1).
    """
    sim = ctrl.ControlSystemSimulation(evaluation_ctrl)
    sim.input['political_match'] = political_score
    sim.input['hobby_match'] = hobby_score
    sim.compute()
    return float(sim.output['overall_match'])


