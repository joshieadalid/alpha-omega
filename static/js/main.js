let mediaRecorder;
let audioChunks = [];

// Iniciar grabación
function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
        .then((stream) => {
            mediaRecorder = new MediaRecorder(stream);
            mediaRecorder.start();

            audioChunks = [];
            mediaRecorder.ondataavailable = (event) => {
                audioChunks.push(event.data);
            };

            console.log("Grabación iniciada");
        })
        .catch((error) => {
            console.error("Error al acceder al micrófono:", error);
        });
}

// Detener grabación y enviar audio
function stopRecording() {
    if (!mediaRecorder) {
        console.warn("No hay una grabación activa.");
        return;
    }

    mediaRecorder.stop();
    mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
        audioChunks = [];
        console.log("Grabación detenida. Enviando audio al servidor...");
        const reply = await sendAudioToServer(audioBlob);
        document.getElementById('responseOutput').textContent = reply || "Error procesando el audio.";
    };
}

