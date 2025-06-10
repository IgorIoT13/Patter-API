document.getElementById('login-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Simulate login process
    if (username && password) {
        alert('Login successful!');
        document.getElementById('login-section').style.display = 'none';
        document.getElementById('device-section').style.display = 'block';

        // Simulate loading devices
        const devices = [
            { id: 1, name: 'Device 1', type: 'Sensor' },
            { id: 2, name: 'Device 2', type: 'Sensor' },
            { id: 3, name: 'Device 3', type: 'Sensor' },
            { id: 4, name: 'Device 4', type: 'Sensor' },
            { id: 5, name: 'Device 5', type: 'Sensor' }
        ];

        const deviceList = document.getElementById('device-list');
        deviceList.innerHTML = '';
        devices.forEach(device => {
            const listItem = document.createElement('li');
            listItem.textContent = `${device.name} (${device.type})`;
            deviceList.appendChild(listItem);
        });
    } else {
        alert('Please enter both username and password.');
    }
});
