import sqlite3
import os
from flask import current_app

class HistoryService:
    @staticmethod
    def get_db_connection():
        db_path = os.path.join(current_app.root_path, '..', 'database', 'alignment.db')
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        return conn

    @classmethod
    def init_db(cls):
        conn = cls.get_db_connection()
        schema_path = os.path.join(current_app.root_path, '..', 'database', 'schema.sql')
        with open(schema_path, 'r') as f:
            conn.executescript(f.read())
        conn.commit()
        conn.close()

    @classmethod
    def save_alignment(cls, params, result):
        conn = cls.get_db_connection()
        conn.execute('''
            INSERT INTO alignments (
                sequence_1, sequence_2, match_score, mismatch_score, 
                gap_penalty, optimization_mode, final_score, 
                aligned_sequence_1, aligned_sequence_2
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            params.sequence_1, params.sequence_2, params.match_score, 
            params.mismatch_score, params.gap_penalty, params.optimization_mode,
            result.score, result.aligned_seq1, result.aligned_seq2
        ))
        conn.commit()
        conn.close()

    @classmethod
    def get_history(cls, limit=10):
        conn = cls.get_db_connection()
        history = conn.execute(
            'SELECT * FROM alignments ORDER BY timestamp DESC LIMIT ?', (limit,)
        ).fetchall()
        conn.close()
        return [dict(row) for row in history]
