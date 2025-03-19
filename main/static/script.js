document.getElementById('passwordform').addEventListener('submit', function (event) {
    event.preventDefault();

    const data = {
        length: document.getElementById('length').value,
        uppercase: document.getElementById('uppercase').checked,
        lowercase: document.getElementById('lowercase').checked,
        numbers: document.getElementById('numbers').checked,
        symbols: document.getElementById('symbols').checked,
    };
    console.log('Dados enviados:', data);

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById('passwordresult').textContent = data.password;
        })
        .catch(error => {
            console.error('Error: ', error);
        });
});
