"""
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const resultDiv = document.getElementById('result');
    const copyBtn = document.getElementById('copyBtn');
    const historyDiv = document.getElementById('history');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(this);
        fetch('/convert', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            resultDiv.textContent = data.text;
            copyBtn.disabled = false;
            loadHistory();
        })
        .catch(error => console.error('Error:', error));
    });

    copyBtn.addEventListener('click', function() {
        navigator.clipboard.writeText(resultDiv.textContent)
        .then(() => {
            alert('Text copied to clipboard');
        })
        .catch(err => {
            console.error('Could not copy text: ', err);
        });
    });

    function loadHistory() {
        fetch('/history')
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            historyDiv.innerHTML = '';
            data.forEach(conversion => {
                const p = document.createElement('p');
                p.textContent = conversion.text;
                historyDiv.appendChild(p);
            });
        })
        .catch(error => console.error('Error:', error));
    }

    loadHistory();
});
"""
