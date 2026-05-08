from typing import List, Tuple
from .models import AlignmentParameters, AlignmentResult
from .scoring import get_scoring_function

def perform_traceback(matrix: List[List[float]], params: AlignmentParameters) -> Tuple[str, str, str, List[Tuple[int, int]]]:
    """Reconstructs the optimal alignment from the DP matrix."""
    seq1 = params.sequence_1
    seq2 = params.sequence_2
    score_func = get_scoring_function(params.match_score, params.mismatch_score, params.optimization_mode)
    
    aligned_seq1 = []
    aligned_seq2 = []
    markers = []
    path = []
    
    i = len(seq1)
    j = len(seq2)
    path.append((i, j))
    
    while i > 0 or j > 0:
        current_score = matrix[i][j]
        
        # Check diagonal move (Match/Mismatch)
        if i > 0 and j > 0:
            char_score = score_func(seq1[i-1], seq2[j-1])
            if current_score == matrix[i-1][j-1] + char_score:
                aligned_seq1.append(seq1[i-1])
                aligned_seq2.append(seq2[j-1])
                markers.append('|' if seq1[i-1] == seq2[j-1] else '.')
                i -= 1
                j -= 1
                path.append((i, j))
                continue
        
        # Check vertical move (Gap in seq2 / Deletion in seq1)
        if i > 0:
            if current_score == matrix[i-1][j] + params.gap_penalty:
                aligned_seq1.append(seq1[i-1])
                aligned_seq2.append('-')
                markers.append(' ')
                i -= 1
                path.append((i, j))
                continue
        
        # Check horizontal move (Gap in seq1 / Insertion in seq2)
        if j > 0:
            if current_score == matrix[i][j-1] + params.gap_penalty:
                aligned_seq1.append('-')
                aligned_seq2.append(seq2[j-1])
                markers.append(' ')
                j -= 1
                path.append((i, j))
                continue
                
        # Safety break if something goes wrong with floating point comparison
        # (Though with integers or simple floats it should be fine)
        break
        
    aligned_seq1.reverse()
    aligned_seq2.reverse()
    markers.reverse()
    path.reverse()
    
    return "".join(aligned_seq1), "".join(aligned_seq2), "".join(markers), path
