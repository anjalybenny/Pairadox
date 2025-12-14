import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

diff_universe = np.arange(0, 9.01, 0.01)
compat_universe = np.arange(0, 1.01, 0.01)

difference = ctrl.Antecedent(diff_universe, 'difference')
compatibility = ctrl.Consequent(compat_universe, 'compatibility')

difference['low'] = fuzz.trimf(difference.universe, [0.0, 0.0, 3.0])
difference['medium'] = fuzz.trapmf(difference.universe, [2.0, 3.5, 5.5, 7.0])
difference['high'] = fuzz.trimf(difference.universe, [6.0, 9.0, 9.0])

compatibility['low'] = fuzz.trimf(compatibility.universe, [0.0, 0.0, 0.4])
compatibility['medium'] = fuzz.trimf(compatibility.universe, [0.2, 0.5, 0.8])
compatibility['high'] = fuzz.trimf(compatibility.universe, [0.6, 1.0, 1.0])

rule_good = ctrl.Rule(difference['low'], compatibility['high'])
rule_ok   = ctrl.Rule(difference['medium'], compatibility['medium'])
rule_bad  = ctrl.Rule(difference['high'], compatibility['low'])

match_ctrl = ctrl.ControlSystem([rule_good, rule_ok, rule_bad])
match_sim = ctrl.ControlSystemSimulation(match_ctrl)


def compute_total_profile_difference(profile_a, profile_b):
    total = 0.0
    for key in profile_a.keys():
        total += abs(profile_a[key] - profile_b[key])
    return total


def compute_compatibility_from_difference(total_difference):
    safe_diff = min(max(float(total_difference), 0.0), 9.0)
    match_sim.input['difference'] = safe_diff
    match_sim.compute()
    return float(match_sim.output['compatibility'])


def compute_compatibility_from_profiles(profile_a, profile_b):
    diff = compute_total_profile_difference(profile_a, profile_b)
    compat = compute_compatibility_from_difference(diff)
    return diff, compat
