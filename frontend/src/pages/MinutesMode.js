import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import {
  startMinutesRecording,
  pauseOrResumeRecording,
  stopMinutesRecording,
  cancelRecording,
} from "../utils/audio-utils-minutes";

function MinutesRecordingApp() {
  const [isRecording, setIsRecording] = useState(false); // Estado para grabación
  const [response, setResponse] = useState(""); // Estado para la respuesta del servidor
  const [audioSrc, setAudioSrc] = useState(""); // Estado para el archivo de audio
  const navigate = useNavigate();

  const handleStartRecording = async () => {
    setIsRecording(true);
    await startMinutesRecording(setResponse); // Inicia la grabación
  };

  const handlePauseResumeRecording = () => {
    pauseOrResumeRecording(setResponse); // Pausa o reanuda la grabación
  };

  const handleStopRecording = () => {
    setIsRecording(false);
    stopMinutesRecording(setResponse, setAudioSrc); // Detiene la grabación y envía el audio
  };

  const handleCancelRecording = () => {
    setIsRecording(false);
    cancelRecording(setResponse); // Cancela la grabación
    setAudioSrc(""); // Limpia el audio grabado
  };

  return (
    <div className="bg-white min-h-screen flex flex-col">
      <header className="p-4 bg-blue-800 text-white text-center font-semibold text-xl">
        Grabación de Minutes y Envío de Peticiones
      </header>

      <main className="flex-1 flex flex-col items-center justify-center p-6">
        {/* Botones de grabación */}
        <div className="mb-6 flex flex-col gap-4 w-full max-w-md">
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
            onClick={handlePauseResumeRecording}
            disabled={!isRecording}
          >
            Pausar/Reanudar
          </button>

          <button
            className={`py-3 px-4 rounded-md font-semibold transition ${
              isRecording
                ? "bg-red-600 text-white hover:bg-red-700"
                : "bg-gray-400 cursor-not-allowed"
            }`}
            onClick={handleStopRecording}
            disabled={!isRecording}
          >
            Detener y Enviar
          </button>

          <button
            className={`py-3 px-4 rounded-md font-semibold transition ${
              isRecording
                ? "bg-gray-800 text-white hover:bg-gray-700"
                : "bg-gray-400 cursor-not-allowed"
            }`}
            onClick={handleCancelRecording}
            disabled={!isRecording}
          >
            Cancelar Grabación
          </button>
        </div>

        {/* Reproductor de audio */}
        {audioSrc && (
          <div className="mt-6 w-full max-w-md">
            <h2 className="font-semibold text-blue-800">Reproducción de Audio</h2>
            <audio src={audioSrc} controls autoPlay className="w-full mt-2" />
          </div>
        )}

        {/* Respuesta del servidor */}
        <div className="mt-6 w-full max-w-md bg-gray-100 p-4 rounded-md">
          <h2 className="font-semibold text-blue-800">Respuesta del servidor</h2>
          <p className="text-gray-700 whitespace-pre-wrap">{response}</p>
        </div>
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

export default MinutesRecordingApp;
