import re
from typing import Tuple, Optional, Any

def validate_sequence(sequence: str) -> Tuple[bool, Optional[str]]:
    if not sequence:
        return False, "Sequence cannot be empty."
    
    # Allow standard biological sequences (DNA, RNA, Protein)
    # For educational purposes, we'll allow alphanumeric but warn or restrict
    # Let's restrict to common biological characters for now
    if not re.match(r"^[A-Z0-9]+$", sequence.upper()):
        return False, "Sequence contains invalid characters. Only alphanumeric characters are allowed."
    
    return True, None

def validate_scoring_param(value: Any, name: str) -> Tuple[bool, Optional[str]]:
    try:
        float(value)
        return True, None
    except (ValueError, TypeError):
        return False, f"{name} must be a numeric value."

def validate_alignment_input(data: dict) -> Tuple[bool, Optional[str]]:
    seq1 = data.get('sequence_1', '')
    seq2 = data.get('sequence_2', '')
    match = data.get('match_score')
    mismatch = data.get('mismatch_score')
    gap = data.get('gap_penalty')
    mode = data.get('optimization_mode')

    valid, msg = validate_sequence(seq1)
    if not valid: return False, f"Sequence 1: {msg}"

    valid, msg = validate_sequence(seq2)
    if not valid: return False, f"Sequence 2: {msg}"

    for val, name in [(match, 'Match score'), (mismatch, 'Mismatch score'), (gap, 'Gap penalty')]:
        valid, msg = validate_scoring_param(val, name)
        if not valid: return False, msg

    if mode not in ['similarity', 'distance']:
        return False, "Invalid optimization mode. Must be 'similarity' or 'distance'."

    return True, None
