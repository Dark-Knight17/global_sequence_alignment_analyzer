import numpy as np
from typing import List, Tuple
from .models import AlignmentParameters, AlignmentResult
from .scoring import get_scoring_function, get_optimization_functions

def initialize_matrix(rows: int, cols: int, gap_penalty: float, mode: str) -> List[List[float]]:
    """Initializes the DP matrix with gap penalties."""
    matrix = [[0.0] * cols for _ in range(rows)]
    
    for i in range(1, rows):
        matrix[i][0] = i * gap_penalty
        
    for j in range(1, cols):
        matrix[0][j] = j * gap_penalty
        
    return matrix

def compute_needleman_wunsch(params: AlignmentParameters) -> Tuple[List[List[float]], float]:
    """Computes the full DP matrix and returns it along with the final score."""
    seq1 = params.sequence_1
    seq2 = params.sequence_2
    rows = len(seq1) + 1
    cols = len(seq2) + 1
    
    matrix = initialize_matrix(rows, cols, params.gap_penalty, params.optimization_mode)
    score_func = get_scoring_function(params.match_score, params.mismatch_score, params.optimization_mode)
    opt_func, _ = get_optimization_functions(params.optimization_mode)
    
    for i in range(1, rows):
        for j in range(1, cols):
            match_score = matrix[i-1][j-1] + score_func(seq1[i-1], seq2[j-1])
            delete_score = matrix[i-1][j] + params.gap_penalty
            insert_score = matrix[i][j-1] + params.gap_penalty
            
            matrix[i][j] = opt_func([match_score, delete_score, insert_score])
            
    final_score = matrix[rows-1][cols-1]
    return matrix, final_score
