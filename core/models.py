from dataclasses import dataclass, field
from typing import List, Tuple, Optional

@dataclass
class AlignmentParameters:
    sequence_1: str
    sequence_2: str
    match_score: float
    mismatch_score: float
    gap_penalty: float
    optimization_mode: str  # 'similarity' or 'distance'

@dataclass
class AlignmentResult:
    aligned_seq1: str
    aligned_seq2: str
    markers: str
    score: float
    matrix: List[List[float]]
    traceback_path: List[Tuple[int, int]]
    parameters: AlignmentParameters
