let mediaRecorder;
let audioChunks = [];
let isPaused = false; // Estado de pausa

async function startRecording() {
    const controlButton = document.getElementById("controlButton");
    const stopButton = document.getElementById("stopButton");
    const cancelButton = document.getElementById("cancelButton");

    try {
        // Obtener permiso del micrófono
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);

        // Manejar los datos de audio
        mediaRecorder.ondataavailable = (event) => {
            audioChunks.push(event.data);
        };

        mediaRecorder.start();
        audioChunks = [];
        isPaused = false;

        // Cambiar el botón a Pausar/Reanudar
        controlButton.innerText = "Pausar";
        controlButton.onclick = pauseOrResumeRecording;

        stopButton.disabled = false;
        cancelButton.disabled = false;

        document.getElementById("responseOutput").innerText = "Grabando...";
    } catch (error) {
        console.error("Error al acceder al micrófono:", error);
        document.getElementById("responseOutput").innerText = "Error al iniciar grabación.";
    }
}

function pauseOrResumeRecording() {
    const controlButton = document.getElementById("controlButton");

    if (mediaRecorder) {
        if (isPaused) {
            mediaRecorder.resume();
            isPaused = false;
            controlButton.innerText = "Pausar";
            document.getElementById("responseOutput").innerText = "Grabando...";
        } else {
            mediaRecorder.pause();
            isPaused = true;
            controlButton.innerText = "Reanudar";
            document.getElementById("responseOutput").innerText = "Grabación pausada.";
        }
    }
}

function stopRecording() {
    const controlButton = document.getElementById("controlButton");
    const stopButton = document.getElementById("stopButton");
    const cancelButton = document.getElementById("cancelButton");

    if (mediaRecorder) {
        mediaRecorder.stop();
        document.getElementById("responseOutput").innerText = "Procesando grabación...";
        mediaRecorder.onstop = async () => {
            const audioBlob = new Blob(audioChunks, { type: "audio/wav" });

            // Enviar el audio al servidor
            const response = await sendAudioToServer(audioBlob);
            document.getElementById("responseOutput").innerText = response.message;

            // Reiniciar botones
            resetButtons();
        };
    }
}

function cancelRecording() {
    const controlButton = document.getElementById("controlButton");
    const stopButton = document.getElementById("stopButton");
    const cancelButton = document.getElementById("cancelButton");

    if (mediaRecorder && mediaRecorder.state !== "inactive") {
        mediaRecorder.stream.getTracks().forEach((track) => track.stop());
        mediaRecorder = null;
        audioChunks = [];
        document.getElementById("responseOutput").innerText = "Grabación cancelada.";
    }

    // Reiniciar botones
    resetButtons();
}

function resetButtons() {
    const controlButton = document.getElementById("controlButton");
    const stopButton = document.getElementById("stopButton");
    const cancelButton = document.getElementById("cancelButton");

    controlButton.innerText = "Iniciar Grabación";
    controlButton.onclick = startRecording;
    controlButton.disabled = false;

    stopButton.disabled = true;
    cancelButton.disabled = true;
}
