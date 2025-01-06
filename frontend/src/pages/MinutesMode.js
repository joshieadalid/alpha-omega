import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

function AudioRecorder() {
  const [message, setMessage] = useState(""); // Estado para el mensaje del usuario
  const [response, setResponse] = useState(""); // Estado para la respuesta del servidor
  const [audioSrc, setAudioSrc] = useState(""); // Estado para la URL del audio
  const [isRecording, setIsRecording] = useState(false); // Estado para grabación
  const [mediaRecorder, setMediaRecorder] = useState(null); // Estado para el MediaRecorder
  const [audioChunks, setAudioChunks] = useState([]); // Fragmentos de audio
  const navigate = useNavigate();

  const handleStartRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream);
      setMediaRecorder(recorder);
      setAudioChunks([]);
      setIsRecording(true);
      setAudioSrc("");

      recorder.ondataavailable = (event) => {
        setAudioChunks((prevChunks) => [...prevChunks, event.data]);
      };

      recorder.start();
    } catch (error) {
      console.error("Error al iniciar la grabación:", error);
      setResponse("Error al iniciar la grabación.");
    }
  };

  const handleStopRecording = async () => {
    if (mediaRecorder) {
      mediaRecorder.stop();
      mediaRecorder.onstop = async () => {
        const audioBlob = new Blob(audioChunks, { type: "audio/ogg" });
        const formData = new FormData();
        formData.append("audio", audioBlob, "audio-recording.ogg");

        try {
          const response = await fetch("http://localhost:8080/api/minutes/audio", {
            method: "POST",
            body: formData,
          });

          if (!response.ok) {
            throw new Error(`Error del servidor: ${response.status}`);
          }

          const data = await response.json();
          setResponse(data.reply || "Respuesta recibida.");
          if (data.audio_url) {
            setAudioSrc(data.audio_url);
          } else {
            setResponse("No se encontró un enlace de audio en la respuesta.");
          }
        } catch (error) {
          console.error("Error al enviar el audio:", error);
          setResponse("Error al enviar el audio al servidor.");
        } finally {
          setIsRecording(false);
        }
      };
    }
  };

  const handleCancelRecording = () => {
    if (mediaRecorder) {
      mediaRecorder.stream.getTracks().forEach((track) => track.stop());
      setMediaRecorder(null);
      setAudioChunks([]);
      setIsRecording(false);
      setResponse("Grabación cancelada.");
    }
  };

  return (
    <div className="bg-white min-h-screen flex flex-col">
      <header className="p-4 bg-blue-800 text-white text-center font-semibold text-xl">
        Grabación de Audio
      </header>

      <main className="flex-1 flex flex-col items-center justify-center p-6">
        <textarea
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Escribe tu mensaje aquí..."
          className="w-full max-w-md p-4 border border-gray-300 rounded-md mb-4"
        ></textarea>

        {/* Botones de grabación */}
        <div className="flex flex-col gap-4">
          <button
            onClick={handleStartRecording}
            disabled={isRecording}
            className={`py-3 px-4 rounded-md font-semibold ${
              isRecording
                ? "bg-gray-400 cursor-not-allowed"
                : "bg-blue-800 text-white hover:bg-blue-700"
            }`}
          >
            Iniciar Grabación
          </button>

          <button
            onClick={handleStopRecording}
            disabled={!isRecording}
            className={`py-3 px-4 rounded-md font-semibold ${
              isRecording
                ? "bg-green-600 text-white hover:bg-green-500"
                : "bg-gray-400 cursor-not-allowed"
            }`}
          >
            Detener y Enviar
          </button>

          <button
            onClick={handleCancelRecording}
            disabled={!isRecording}
            className={`py-3 px-4 rounded-md font-semibold ${
              isRecording
                ? "bg-red-600 text-white hover:bg-red-500"
                : "bg-gray-400 cursor-not-allowed"
            }`}
          >
            Cancelar
          </button>
        </div>

        {/* Respuesta del servidor */}
        <div className="mt-6 bg-gray-100 text-blue-800 p-4 rounded-md text-center w-full max-w-md">
          {response || "Aquí aparecerá la respuesta del servidor."}
        </div>

        {/* Reproductor de audio */}
        {audioSrc && (
          <div className="mt-6 w-full max-w-md">
            <h2 className="font-semibold text-blue-800">Reproducir Audio</h2>
            <audio src={audioSrc} controls autoPlay className="w-full mt-2" />
          </div>
        )}
      </main>

      <footer className="p-4 flex justify-center items-center">
        <button
          onClick={() => navigate("/menu")}
          className="bg-blue-800 text-white py-2 px-6 rounded-lg shadow-md hover:bg-blue-700 flex items-center gap-2"
        >
          <i className="fas fa-arrow-left text-lg"></i>
          Menú Principal
        </button>
      </footer>
    </div>
  );
}

export default AudioRecorder;
