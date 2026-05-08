# Global_Sequence_Alignment_Analyzer

Global_Sequence_Alignment_Analyzer is a professional educational bioinformatics web application designed to teach and demonstrate the **Needleman-Wunsch algorithm** for global sequence alignment.

## 🧬 Overview

Sequence alignment is a fundamental task in bioinformatics used to identify regions of similarity that may indicate functional, structural, or evolutionary relationships between biological sequences (DNA, RNA, or Protein).

This platform provides a visual and interactive way to:
- Perform global sequence alignment between two strings.
- Visualize the **Dynamic Programming (DP)** matrix used in the algorithm.
- Trace the optimal path from the end of the sequences back to the start.
- Understand the biological and mathematical significance of every step.

## 🚀 Features

- **Needleman-Wunsch Implementation**: Robust core algorithm for global alignment.
- **Interactive Scoring**: Customize Match, Mismatch, and Gap penalties.
- **Optimization Modes**: 
  - **Similarity**: Maximize the alignment score (commonly used for DNA/Protein).
  - **Distance**: Minimize the edit/evolutionary distance.
- **DP Matrix Visualization**: High-resolution grid showing score calculations and the traceback path.
- **Educational Walkthroughs**: Plain-English explanations for Initialization, Filling, and Traceback.
- **Biological Context**: Insights into what gaps and mismatches represent in evolution.
- **History Tracking**: Automatically saves your alignments to a local SQLite database for later review.

## 🛠️ Technology Stack

- **Backend**: Python 3.12+, Flask
- **Frontend**: Modern Vanilla CSS, JavaScript (ES6+), Jinja2 Templates
- **Database**: SQLite
- **Numerical Processing**: NumPy

## 📂 Architecture

The project follows a modular, layered architecture:
- `core/`: Pure algorithmic logic (Alignment, Scoring, Traceback, Validation).
- `app/services/`: Orchestration layer connecting core logic with the web interface.
- `app/routes/`: Flask blueprints for handling web requests.
- `app/static/`: Frontend assets (CSS/JS).
- `app/templates/`: UI layouts.
- `database/`: Persistence layer (Schema and SQLite DB).

## 🔧 Setup & Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd Global_Sequence_Alignment_Analyzer
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python run.py
   ```
   The application will be available at `http://127.0.0.1:5000`.

## 🧠 The Needleman-Wunsch Algorithm

The algorithm follows three main phases:
1. **Initialization**: Setting up the matrix and applying initial gap penalties.
2. **Matrix Filling**: Using dynamic programming to calculate the optimal score for every possible sub-alignment.
3. **Traceback**: Reconstructing the actual alignment by following the path of optimal scores from the bottom-right to the top-left.

## 🤝 Contributing

This is an educational project. Contributions that improve the clarity of explanations or the quality of visualizations are welcome!

## 📜 License

MIT License
