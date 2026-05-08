CREATE TABLE IF NOT EXISTS alignments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sequence_1 TEXT NOT NULL,
    sequence_2 TEXT NOT NULL,
    match_score REAL NOT NULL,
    mismatch_score REAL NOT NULL,
    gap_penalty REAL NOT NULL,
    optimization_mode TEXT NOT NULL,
    final_score REAL NOT NULL,
    aligned_sequence_1 TEXT NOT NULL,
    aligned_sequence_2 TEXT NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
);
