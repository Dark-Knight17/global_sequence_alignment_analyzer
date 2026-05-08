from .models import AlignmentParameters, AlignmentResult

def get_algorithm_explanations(result: AlignmentResult) -> dict:
    params = result.parameters
    mode = params.optimization_mode
    
    explanations = {
        "initialization": {
            "title": "Matrix Initialization",
            "content": (
                f"We start by creating a grid of size {len(params.sequence_1)+1}x{len(params.sequence_2)+1}. "
                f"The first row and column represent alignments against gaps (denoted as λ). "
                f"Since every gap costs {params.gap_penalty}, we fill them with cumulative penalties: "
                f"0, {params.gap_penalty}, {2*params.gap_penalty}, etc."
            )
        },
        "filling": {
            "title": "Matrix Filling (Dynamic Programming)",
            "content": (
                f"We fill the matrix cell by cell. For each cell (i, j), we look at three possible moves: "
                "1. Diagonal: Aligning character i from Seq1 with character j from Seq2. "
                f"Score = Diagonal Cell + ({params.match_score} if match, else {params.mismatch_score}). "
                "2. Vertical: A gap in Seq2. Score = Top Cell + gap penalty. "
                "3. Horizontal: A gap in Seq1. Score = Left Cell + gap penalty. "
                f"Because we are in '{mode}' mode, we choose the {'maximum' if mode=='similarity' else 'minimum'} of these three values."
            )
        },
        "traceback": {
            "title": "Traceback Path",
            "content": (
                "Once the matrix is full, we start from the bottom-right corner and work backwards. "
                "At each step, we identify which of the three neighbor cells produced the current score. "
                "A diagonal move means an alignment (match or mismatch), while vertical/horizontal moves represent insertions or deletions (gaps)."
            )
        },
        "biological": {
            "title": "Biological Interpretation",
            "content": (
                "In biology, sequence alignment helps identify evolutionary relationships. "
                "Matches ('|') suggest conserved regions, while mismatches ('.') indicate mutations. "
                "Gaps (spaces) represent insertions or deletions (indels) that occurred over time. "
                f"Our final alignment score of {result.score} quantifies the {'similarity' if mode=='similarity' else 'evolutionary distance'} between these two sequences."
            )
        }
    }
    return explanations
