document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('alignment-form');
    const resultsSection = document.getElementById('results-section');
    const loading = document.getElementById('loading');
    const errorDiv = document.getElementById('error-message');
    const historyList = document.getElementById('history-list');
    const refreshHistoryBtn = document.getElementById('refresh-history');

    // Load history on startup
    loadHistory();

    refreshHistoryBtn.addEventListener('click', loadHistory);

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        // Reset UI
        resultsSection.classList.add('hidden');
        errorDiv.classList.add('hidden');
        loading.classList.remove('hidden');

        const formData = new FormData(form);
        const data = Object.fromEntries(formData.entries());

        try {
            const response = await fetch('/align', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify(data)
            });

            const result = await response.json();

            if (result.success) {
                renderResults(result.result);
                resultsSection.classList.remove('hidden');
                loadHistory(); // Refresh history after new alignment
            } else {
                showError(result.error);
            }
        } catch (err) {
            showError("An unexpected error occurred. Please check your connection.");
            console.error(err);
        } finally {
            loading.classList.add('hidden');
        }
    });

    async function loadHistory() {
        try {
            const response = await fetch('/history?limit=5');
            const data = await response.json();
            if (data.success) {
                renderHistory(data.history);
            }
        } catch (err) {
            console.error("Failed to load history", err);
        }
    }

    function renderHistory(history) {
        if (!history || history.length === 0) {
            historyList.innerHTML = '<p>No recent alignments found.</p>';
            return;
        }

        historyList.innerHTML = history.map(item => `
            <div class="history-item">
                <div class="history-info">
                    <div class="history-seqs">${item.sequence_1} vs ${item.sequence_2}</div>
                    <div class="history-meta">${item.optimization_mode} | Match: ${item.match_score} | Score: ${item.final_score}</div>
                </div>
                <div class="history-time">${new Date(item.timestamp).toLocaleString()}</div>
            </div>
        `).join('');
    }

    function renderResults(data) {
        // Render Alignment
        const alignmentOutput = document.getElementById('alignment-output');
        alignmentOutput.textContent = `${data.aligned_seq1}\n${data.markers}\n${data.aligned_seq2}`;
        
        const scoreDisplay = document.getElementById('final-score');
        scoreDisplay.textContent = `Final Score: ${data.score}`;

        // Render Matrix
        renderMatrix(data.matrix_data);

        // Render Explanations
        renderExplanations(data.explanations);
    }

    function renderMatrix(matrixData) {
        const table = document.getElementById('dp-matrix');
        table.innerHTML = '';

        const { matrix, path, seq1, seq2 } = matrixData;
        
        // Header Row (Seq2)
        const headerRow = document.createElement('tr');
        headerRow.appendChild(document.createElement('th')); // Empty corner
        headerRow.appendChild(document.createElement('th')).textContent = 'λ';
        seq2.forEach(char => {
            const th = document.createElement('th');
            th.textContent = char;
            headerRow.appendChild(th);
        });
        table.appendChild(headerRow);

        // Matrix Rows
        matrix.forEach((row, i) => {
            const tr = document.createElement('tr');
            
            // Row Label (Seq1)
            const labelTh = document.createElement('th');
            labelTh.textContent = i === 0 ? 'λ' : seq1[i-1];
            tr.appendChild(labelTh);

            row.forEach((val, j) => {
                const td = document.createElement('td');
                td.textContent = val;
                
                // Check if in path
                if (path.some(([pi, pj]) => pi === i && pj === j)) {
                    td.classList.add('path-cell');
                }
                
                tr.appendChild(td);
            });
            table.appendChild(tr);
        });
    }

    function renderExplanations(explanations) {
        const section = document.getElementById('explanations-section');
        section.innerHTML = '';

        const order = ['initialization', 'filling', 'traceback', 'biological'];
        order.forEach(key => {
            const exp = explanations[key];
            const div = document.createElement('div');
            div.className = 'explanation-card';
            div.innerHTML = `
                <h3>${exp.title}</h3>
                <p>${exp.content}</p>
            `;
            section.appendChild(div);
        });
    }

    function showError(msg) {
        errorDiv.textContent = msg;
        errorDiv.classList.remove('hidden');
    }
});
