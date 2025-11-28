import numpy as np
import skfuzzy as fuzz

class FuzzyMatcher:
    def __init__(self):
        # There are 30 questions. Max diff per question is 1.0.
        # Max Total Diff = 30.0.
        self.x_diff = np.arange(0, 31, 0.1)

        # SCALING: Total difference ranges from 0 to 30.
        
        # Low difference = Bad Match (0 to ~10)
        self.diff_low = fuzz.trimf(self.x_diff, [0, 0, 10])
         
        # Medium difference = Average Match (~8 to ~20)
        self.diff_medium = fuzz.trapmf(self.x_diff, [8, 12, 18, 22])
        
        # High difference = Good Match (~18 to 30)
        self.diff_high = fuzz.trimf(self.x_diff, [18, 30, 30])

    def get_fuzzy_match_level(self, total_difference):
        """
        Calculates how much the total difference belongs to Low, Medium, or High.
        """
        # Clamp value to max 30 to avoid errors
        safe_diff = min(total_difference, 30.0)

        # Calculate membership degrees
        level_low = fuzz.interp_membership(self.x_diff, self.diff_low, safe_diff)
        level_med = fuzz.interp_membership(self.x_diff, self.diff_medium, safe_diff)
        level_high = fuzz.interp_membership(self.x_diff, self.diff_high, safe_diff)

        return {
            "low": level_low,      # Low Compatibility
            "medium": level_med,   # Medium Compatibility
            "high": level_high     # High Compatibility
        }

    def visualize(self):
        import matplotlib.pyplot as plt
        plt.figure(figsize=(8, 5))
        plt.plot(self.x_diff, self.diff_low, 'g', linewidth=1.5, label='Low Diff (Bad Match)')
        plt.plot(self.x_diff, self.diff_medium, 'b', linewidth=1.5, label='Medium Diff')
        plt.plot(self.x_diff, self.diff_high, 'r', linewidth=1.5, label='High Diff (Good Match)')
        plt.title('Fuzzy Membership Functions (Scale 0-30)')
        plt.legend()
        plt.show()