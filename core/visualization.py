from typing import List, Tuple, Dict
from .models import AlignmentResult

def prepare_matrix_for_ui(result: AlignmentResult) -> Dict:
    """Prepares the matrix and traceback path for frontend display."""
    matrix = result.matrix
    path = result.traceback_path
    seq1 = result.parameters.sequence_1
    seq2 = result.parameters.sequence_2
    
    # Create a grid with labels
    # Row 0: Labels for seq2
    # Col 0: Labels for seq1
    
    formatted_matrix = []
    # Header row
    header = ["", ""] + list(seq2)
    formatted_matrix.append(header)
    
    # First row of matrix (gap row)
    first_row = ["", "λ"] + [str(val) for val in matrix[0]]
    formatted_matrix.append(first_row)
    
    for i in range(1, len(matrix)):
        row = [seq1[i-1], "λ" if i==0 else seq1[i-1]] # Adjusting for visual
        # Actually, let's keep it simple:
        # Row labels are Seq1 chars
        # Col labels are Seq2 chars
        pass

    # Let's rethink the structure for better JS rendering
    return {
        "matrix": matrix,
        "path": path,
        "seq1": list(seq1),
        "seq2": list(seq2),
        "score": result.score
    }

def format_alignment_output(result: AlignmentResult) -> str:
    """Formats the alignment for console or simple text display."""
    return f"{result.aligned_seq1}\n{result.markers}\n{result.aligned_seq2}\n\nScore: {result.score}"
