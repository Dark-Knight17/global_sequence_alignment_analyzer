from typing import Callable

def get_scoring_function(match: float, mismatch: float, mode: str) -> Callable[[str, str], float]:
    """Returns a function that calculates the score between two characters."""
    def score_chars(char1: str, char2: str) -> float:
        if char1 == char2:
            return match
        else:
            return mismatch
    return score_chars

def get_optimization_functions(mode: str):
    """Returns (extreme_value_finder, comparison_operator)."""
    if mode == 'similarity':
        return max, lambda a, b: a > b
    else: # distance
        return min, lambda a, b: a < b
