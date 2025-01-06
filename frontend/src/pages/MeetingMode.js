import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  startRecording,
  pauseOrResumeRecording,
  stopRecording,
  cancelRecording,
} from "../utils/audio-utils";

function AudioRecorder() {
  const [isRecording, setIsRecording] = useState(false); // Estado para grabación
  const [isPaused, setIsPaused] = useState(false); // Estado para pausa
  const [response, setResponse] = useState(""); // Estado para mostrar resultados
  const [audioSrc, setAudioSrc] = useState(""); // Estado para la URL del audio
  const navigate = useNavigate();

  const handleStartRecording = async () => {
    setIsRecording(true);
    setIsPaused(false);
    setAudioSrc(""); // Limpiar cualquier audio previo
    await startRecording(setResponse);
  };

  const handlePauseOrResumeRecording = () => {
    pauseOrResumeRecording(setResponse);
    setIsPaused((prev) => !prev);
  };

  const handleStopRecording = async () => {
    setIsRecording(false);
    setIsPaused(false);
    stopRecording((serverResponse) => {
      try {
        const responseJSON = JSON.parse(serverResponse); // Parsear JSON de la respuesta
        setResponse(responseJSON.reply || "Respuesta recibida.");
        if (responseJSON.audio_url) {
          setAudioSrc(responseJSON.audio_url); // Actualizar la URL del audio
        } else {
          setResponse("No se encontró un audio en la respuesta.");
        }
      } catch (error) {
        console.error("Error al parsear la respuesta:", error);
        setResponse("Error al procesar la respuesta del servidor.");
      }
    });
  };

  const handleCancelRecording = () => {
    setIsRecording(false);
    setIsPaused(false);
    cancelRecording(setResponse);
    setAudioSrc(""); // Limpiar cualquier audio previo
  };

  return (
    <div className="bg-white min-h-screen flex flex-col">
      <header className="p-4 bg-blue-800 text-white text-center font-semibold text-xl">
        Grabación de Audio
      </header>

      <main className="flex-1 flex flex-col items-center justify-center p-6">
        {/* Botones de grabación */}
        <div className="flex flex-col gap-4">
          <button
            className={`py-3 px-4 rounded-md font-semibold transition ${
              isRecording
                ? "bg-gray-400 cursor-not-allowed"
                : "bg-blue-800 text-white hover:bg-blue-700"
            }`}
            onClick={handleStartRecording}
            disabled={isRecording}
          >
            Iniciar Grabación
          </button>

          <button
            className={`py-3 px-4 rounded-md font-semibold transition ${
              isRecording
                ? "bg-yellow-600 text-white hover:bg-yellow-500"
                : "bg-gray-400 cursor-not-allowed"
            }`}
            onClick={handlePauseOrResumeRecording}
            disabled={!isRecording}
          >
            {isPaused ? "Reanudar Grabación" : "Pausar Grabación"}
          </button>

          <button
            className={`py-3 px-4 rounded-md font-semibold transition ${
              isRecording
                ? "bg-green-600 text-white hover:bg-green-500"
                : "bg-gray-400 cursor-not-allowed"
            }`}
            onClick={handleStopRecording}
            disabled={!isRecording}
          >
            Detener y Enviar
          </button>

          <button
            className={`py-3 px-4 rounded-md font-semibold transition border ${
              isRecording
                ? "border-red-600 text-red-600 hover:bg-red-600 hover:text-white"
                : "border-gray-400 text-gray-400 cursor-not-allowed"
            }`}
            onClick={handleCancelRecording}
            disabled={!isRecording}
          >
            Cancelar
          </button>
        </div>

        {/* Respuesta del servidor */}
        <div className="mt-6 bg-gray-100 text-blue-800 p-4 rounded-md text-center w-full max-w-md">
          {response || "Aquí aparecerá la respuesta del servidor."}
        </div>

        {/* Reproductor de audio */}
        {audioSrc ? (
          <div className="mt-6 w-full max-w-md">
            <h2 className="font-semibold text-blue-800">Reproducir Audio</h2>
            <audio
              src={audioSrc}
              controls
              autoPlay
              className="w-full mt-2 border border-gray-300 rounded-md"
            />
          </div>
        ) : (
          <p className="mt-6 text-gray-500">No hay audio disponible.</p>
        )}
      </main>

      {/* Botón de regreso al menú principal */}
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
