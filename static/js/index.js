let mediaRecorder;
let audioChunks = [];

async function sendMessage() {
    const message = document.getElementById("message").value;
    const responseElement = document.getElementById("response");

    responseElement.innerText = "Cargando respuesta...";

    try {
        const response = await fetch("/chatbot", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const data = await response.json();
        console.log("Datos recibidos:", data); // Para depuración

        // Accede a la lista de proyectos en `data.reply`
        if (data.reply && data.reply.values && Array.isArray(data.reply.values) && data.reply.values.length > 0) {
            const projects = data.reply.values.map(project => `Proyecto: ${project.name} - Key: ${project.key}`).join(", ");
            responseElement.innerText = `Proyectos recientes: ${projects}`;
        } else {
            responseElement.innerText = "No se encontraron proyectos recientes.";
        }
    } catch (error) {
        responseElement.innerText = "Error al conectar con el chatbot.";
        console.error("Error:", error);
    }
}



async function startRecording() {
    const responseElement = document.getElementById("response");
    responseElement.innerText = "Preparando grabación...";

    try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        mediaRecorder = new MediaRecorder(stream);

        mediaRecorder.onstart = () => {
            audioChunks = [];
            responseElement.innerText = "Grabando...";
            document.querySelector("button[onclick='stopRecording()']").disabled = false;
        };

        mediaRecorder.ondataavailable = event => {
            audioChunks.push(event.data);
        };

        mediaRecorder.onstop = () => {
            const audioBlob = new Blob(audioChunks, { type: "audio/wav" });
            sendAudioToServer(audioBlob);
            responseElement.innerText = "Grabación finalizada. Enviando al servidor...";
            document.querySelector("button[onclick='stopRecording()']").disabled = true;
        };

        mediaRecorder.start();
    } catch (error) {
        console.error("Error al acceder al micrófono:", error);
        responseElement.innerText = "No se pudo acceder al micrófono.";
    }
}

function stopRecording() {
    if (mediaRecorder) {
        mediaRecorder.stop();
    }
}

async function sendAudioToServer(audioBlob) {
    const formData = new FormData();
    formData.append("audio", audioBlob, "recording.wav");

    try {
        const response = await fetch("/chatbot", {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const data = await response.json();
        document.getElementById("response").innerText = data.reply;
    } catch (error) {
        document.getElementById("response").innerText = "Error al enviar el audio.";
        console.error("Error:", error);
    }
}
