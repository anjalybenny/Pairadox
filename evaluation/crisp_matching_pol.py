

# crisp_matching.py

class CrispMatcher:
    def get_match_label(self, total_difference):
        """
        Returns a single distinct category based on hard thresholds.
        """
        # We use thresholds roughly based on your fuzzy sets intersections:
        # 0 - 11: Low Difference (Good Match)
        # 11 - 21: Medium Difference (Average Match)
        # 21 - 30: High Difference (Bad Match)
        
        if total_difference < 10:
            return 1.0, 0.0, 0.0
        elif total_difference < 21:
            return 0.0, 1.0, 0.0
        else:
            return 0.0, 0.0, 1.0