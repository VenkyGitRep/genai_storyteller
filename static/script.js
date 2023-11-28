document.getElementById('generate-btn').addEventListener('click', function(e) {
    e.preventDefault();

    const promptText = document.getElementById('prompt').value;
    const outputDiv = document.getElementById('generated-story');

    fetch('http://127.0.0.1:5000/generate-text', {  // Update this URL to match your Flask route
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ prompt: promptText })
    })
    .then(response => response.json())
    .then(data => {
        outputDiv.textContent = data.text_response; 
        console.log(data.generatedText) // Update this to match the key in your response JSON
    })
    .catch(error => {
        console.error('Error:', error);
        outputDiv.textContent = 'Error generating text. Please try again.';
    });
});
