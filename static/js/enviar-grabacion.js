async function sendAudioToServer(audioBlob) {
    try {
        const formData = new FormData();

        // Agrega el audio con un nombre y extensión
        formData.append('audio', audioBlob, 'audio_recording.wav');

        // Envía el audio al servidor
        const response = await fetch('/chatbot/meeting_audio', {
            method: 'POST',
            body: formData,
        });

        // Verifica si la respuesta es exitosa
        if (!response.ok) {
            try {
                const errorData = await response.json();
                console.error("Error en el servidor (JSON):", errorData);
                return `Error del servidor: ${JSON.stringify(errorData)}`;
            } catch {
                const errorText = await response.text();
                console.error("Error en el servidor (texto):", errorText);
                return `Error del servidor: ${errorText}`;
            }
        }

        // Procesa la respuesta exitosa
        try {
            const data = await response.json();
            console.log("Respuesta del servidor (JSON):", data);
            return `Respuesta: ${JSON.stringify(data)}`;
        } catch {
            const text = await response.text();
            console.log("Respuesta del servidor (texto):", text);
            return `Respuesta: ${text}`;
        }
    } catch (error) {
        console.error("Error al enviar el audio:", error);
        return `Error al enviar el audio: ${error.message}`;
    }
}
