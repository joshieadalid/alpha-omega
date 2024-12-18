// Subir audio al servidor
async function sendAudioToServer(audioBlob) {
    const formData = new FormData();
    formData.append('audio', audioBlob);

    try {
        const response = await fetch(`/chatbot/audio`, {
            method: 'POST',
            body: formData,
        });

        if (response.ok) {
            const data = await response.json();
            console.log("Respuesta del servidor:", data.reply);
            return data.reply;
        } else {
            console.error("Error al enviar el audio:", response.statusText);
        }
    } catch (error) {
        console.error("Error al conectarse al servidor:", error);
    }
}
