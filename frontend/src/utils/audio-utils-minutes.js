let mediaRecorder;
let audioChunks = [];
let isPaused = false;

// Base URL de la API
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || "http://localhost:8080";

export async function startMinutesRecording(setResponse) {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (event) => {
      audioChunks.push(event.data);
    };

    mediaRecorder.start();
    audioChunks = [];
    isPaused = false;

    setResponse("Grabando para minutes...");
  } catch (error) {
    console.error("Error al iniciar grabación:", error);
    setResponse("Error al iniciar grabación.");
  }
}

export function pauseOrResumeRecording(setResponse) {
  if (mediaRecorder) {
    if (isPaused) {
      mediaRecorder.resume();
      isPaused = false;
      setResponse("Grabación reanudada.");
    } else {
      mediaRecorder.pause();
      isPaused = true;
      setResponse("Grabación pausada.");
    }
  }
}

export function stopMinutesRecording(setResponse, setAudioSrc) {
  if (mediaRecorder) {
    mediaRecorder.stop();
    mediaRecorder.onstop = async () => {
      const audioBlob = new Blob(audioChunks, { type: "audio/ogg" });
      audioChunks = []; // Limpiar los fragmentos después de detener la grabación

      const response = await sendMinutesAudioToServer(audioBlob, setAudioSrc);
      setResponse(response.message || "Grabación enviada con éxito.");
    };
  }
}

export function cancelRecording(setResponse) {
  if (mediaRecorder && mediaRecorder.state !== "inactive") {
    mediaRecorder.stream.getTracks().forEach((track) => track.stop());
    mediaRecorder = null;
    audioChunks = [];
    isPaused = false;
    setResponse("Grabación cancelada.");
  }
}

export async function sendMinutesAudioToServer(audioBlob, setAudioSrc) {
  try {
    const formData = new FormData();
    formData.append("audio", audioBlob, "audio-recording.ogg");

    const response = await fetch(`${API_BASE_URL}/api/minutes/audio`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errorText = await response.text();
      return { error: `Error del servidor: ${errorText}` };
    }

    const data = await response.json();

    // Asignar la URL del audio al reproductor si está presente
    if (data.audio_url) {
      setAudioSrc(data.audio_url);
    }

    return {
      message: data.reply || "Respuesta del servidor recibida.",
      audioUrl: data.audio_url || null,
    };
  } catch (error) {
    console.error("Error al enviar audio:", error);
    return { error: `Error al enviar audio: ${error.message}` };
  }
}
