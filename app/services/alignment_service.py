from core.models import AlignmentParameters, AlignmentResult
from core.alignment import compute_needleman_wunsch
from core.traceback import perform_traceback
from core.validation import validate_alignment_input
from core.visualization import prepare_matrix_for_ui
from core.explanations import get_algorithm_explanations

class AlignmentService:
    @staticmethod
    def run_alignment(data: dict) -> dict:
        """Main entry point for running an alignment."""
        # Validate
        is_valid, error_msg = validate_alignment_input(data)
        if not is_valid:
            return {"success": False, "error": error_msg}
        
        # Prepare parameters
        params = AlignmentParameters(
            sequence_1=data['sequence_1'],
            sequence_2=data['sequence_2'],
            match_score=float(data['match_score']),
            mismatch_score=float(data['mismatch_score']),
            gap_penalty=float(data['gap_penalty']),
            optimization_mode=data['optimization_mode']
        )
        
        # Align
        matrix, final_score = compute_needleman_wunsch(params)
        
        # Traceback
        seq1_aln, seq2_aln, markers, path = perform_traceback(matrix, params)
        
        # Package result
        result = AlignmentResult(
            aligned_seq1=seq1_aln,
            aligned_seq2=seq2_aln,
            markers=markers,
            score=final_score,
            matrix=matrix,
            traceback_path=path,
            parameters=params
        )
        
        # Get UI data and explanations
        ui_data = prepare_matrix_for_ui(result)
        explanations = get_algorithm_explanations(result)
        
        return {
            "success": True, 
            "result": {
                "aligned_seq1": result.aligned_seq1,
                "aligned_seq2": result.aligned_seq2,
                "markers": result.markers,
                "score": result.score,
                "matrix_data": ui_data,
                "explanations": explanations
            }
        }
