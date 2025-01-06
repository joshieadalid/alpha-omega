import { useState } from "react";

// Variables globales para grabación
let mediaRecorder;
let audioChunks = [];
let isPaused = false;

// Base URL de la API
const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || "http://localhost:8080";

export async function startRecording(setResponse) {
  try {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorder = new MediaRecorder(stream);

    mediaRecorder.ondataavailable = (event) => {
      audioChunks.push(event.data);
    };

    mediaRecorder.start();
    audioChunks = [];
    isPaused = false;

    setResponse("Grabando...");
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
      setResponse("Grabando...");
    } else {
      mediaRecorder.pause();
      isPaused = true;
      setResponse("Grabación pausada.");
    }
  }
}

export function stopRecording(setResponse) {
  if (mediaRecorder) {
    mediaRecorder.stop();
    mediaRecorder.onstop = async () => {
      const audioBlob = new Blob(audioChunks, { type: "audio/ogg" });
      audioChunks = []; // Limpiar los fragmentos después de enviarlos
      const response = await sendAudioToServer(audioBlob);
      setResponse(response);
    };
  }
}

export function cancelRecording(setResponse) {
  if (mediaRecorder && mediaRecorder.state !== "inactive") {
    mediaRecorder.stream.getTracks().forEach((track) => track.stop());
    mediaRecorder = null;
    audioChunks = [];
    setResponse("Grabación cancelada.");
  }
}

export async function sendAudioToServer(audioBlob) {
  try {
    const formData = new FormData();
    formData.append("audio", audioBlob, "audio-recording.ogg");

    const response = await fetch(`${API_BASE_URL}/api/meeting_audio`, {
      method: "POST",
      body: formData,
    });

    if (!response.ok) {
      const errorText = await response.text();
      return `Error del servidor: ${errorText}`;
    }

    const data = await response.json();
    return data.reply || "Respuesta del servidor recibida.";
  } catch (error) {
    console.error("Error al enviar audio:", error);
    return `Error al enviar audio: ${error.message}`;
  }
}
