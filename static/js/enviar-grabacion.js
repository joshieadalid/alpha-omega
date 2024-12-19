import { ElevenLabsClient } from "elevenlabs";

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

async function textToSpeechStream(text) {
    const client = new ElevenLabsClient({ apiKey: 'ELEVENLABS_API_KEY' });
    const voiceId = 'SvU0B5XIX9vlVyFfY2Kc'; // ID de voz de Idalia
    const modelId = 'eleven_multilingual_v2'; // Modelo TTS a utilizar

    // Realizar la solicitud de TTS en modo streaming
    try {
        // Realizar la solicitud de TTS en modo streaming
        const audioStream = await client.textToSpeech.convertAsStream(voiceId, {
            text,
            model_id: modelId,
            output_format: "mp3_44100_128",
        });

        // Crear un contexto de audio
        const audioChunks = [];
        const reader = audioStream.getReader();

        // Leer datos del flujo
        while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            audioChunks.push(value);
        }

        // Verificar que se hayan recibido datos
        if (audioChunks.length === 0) {
            console.error("No se recibieron datos de audio");
            return;
        }

        // Convertir los fragmentos en un Blob reproducible
        const audioBlob = new Blob(audioChunks, { type: 'audio/mpeg' });
        const audioURL = URL.createObjectURL(audioBlob);

        // Reproducir el audio
        const audio = new Audio(audioURL);
        audio.play();
    } catch (error) {
        console.error("Error al generar o reproducir el audio:", error);
    }
}
// const voiceId = 'w56kEoqD0CoEldmNCYKE'; // ID de voz de Farid Dieck
    // const voiceId = 'wJqPPQ618aTW29mptyoc'; // ID de voz de Ana 
    // const voiceId = 'LcfcDJNUP1GQjkzn1xUU'; // ID de voz de Emily
    // const voiceID = 'zcAOhNBS3c14rBihAFp1'; // ID de voz de Giovanni
