async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return;

    const chatBox = document.getElementById('chat-box');
    chatBox.innerHTML += `<div class="user-message"><b>You:</b> ${userInput}</div>`;

    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();
    if (data.error) {
        chatBox.innerHTML += `<div class="error-message"><b>Error:</b> ${data.error}</div>`;
    } else {
        chatBox.innerHTML += `<div class="response-message"><b>${data.source.toUpperCase()}:</b> ${data.response} <i>${data.sentiment ? '(' + data.sentiment + ' sentiment)' : ''}</i></div>`;
    }

    document.getElementById('user-input').value = '';
}
