function fetchAvatar() {
    fetch('/random-avatar')
        .then(response => response.json())
        .then(data => {
            if (data.success === false) {
                alert(data.message);
                return;
            }

            const avatarContainer = document.getElementById('avatar-container');
            const avatarImg = document.getElementById('avatar-img');
            const downloadLink = document.getElementById('download-link');

            avatarImg.src = `/static/avatars/${data.filename}`;
            avatarContainer.classList.remove('hidden');
            document.getElementById('error-message').classList.add('hidden');

            const updateDownloadLink = () => {
                const format = document.getElementById('format').value;
                const width = document.getElementById('width').value;
                const height = document.getElementById('height').value;
                downloadLink.href = `/download/${data.id}/${format}/${width}/${height}`;
            };

            document.getElementById('format').addEventListener('change', updateDownloadLink);
            document.getElementById('width').addEventListener('input', updateDownloadLink);
            document.getElementById('height').addEventListener('input', updateDownloadLink);

            updateDownloadLink();
        })
        .catch(error => {
            console.error('Error getting random avatar:', error);
        });
}

document.getElementById('get-avatar-btn').addEventListener('click', fetchAvatar);

document.getElementById('download-link').addEventListener('click', (event) => {
    event.preventDefault();
    const downloadLink = event.target.href;
    fetch(downloadLink)
        .then(response => {
            if (!response.ok) {
                return response.json().then(data => {
                    throw new Error(data.message);
                });
            }
            return response.blob().then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.style.display = 'none';
                a.href = url;
                a.download = downloadLink.split('/').pop();
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
            });
        })
        .catch(error => {
            const errorMessage = document.getElementById('error-message');
            errorMessage.textContent = error.message;
            errorMessage.classList.remove('hidden');
        });
});

// Fetch an avatar immediately when the page loads
window.onload = fetchAvatar;
