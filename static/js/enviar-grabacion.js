async function sendAudioToServer(audioBlob) {
    try {
        const formData = new FormData();

        // Agrega el audio con un nombre y extensión
        formData.append('audio', audioBlob, 'audio-recording.ogg');

        // Envía el audio al servidor
        const response = await fetch('/api/meeting_audio', {
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

            // Verifica si el atributo 'reply' existe
            if ('reply' in data) {
                return `Respuesta: ${data.reply}`;
            } else {
                console.error("El JSON no contiene el atributo 'reply':", data);
                return "Error: El servidor no devolvió el atributo 'reply'.";
            }
        } catch {
            const text = await response.text();
            console.log("Respuesta del servidor (texto):", text);
            textToSpeechStream(text);
            return `Respuesta: ${text}`;
        }
    } catch (error) {
        console.error("Error al enviar el audio:", error);
        return `Error al enviar el audio: ${error.message}`;
    }
}

