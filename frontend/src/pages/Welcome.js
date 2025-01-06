import React from "react";
import { useNavigate } from "react-router-dom";
import Header from "../components/Header";
import Footer from "../components/Footer";

function WelcomeScreen() {
  const navigate = useNavigate();

  return (
    <div className="bg-gray-100 min-h-screen flex flex-col">
      {/* Header */}
      <Header />

      {/* Quick Access Buttons */}
      <div className="absolute top-24 right-4 flex gap-4 z-50">
        <button
          onClick={() => navigate("/login")}
          className="bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded-lg text-sm shadow-lg transition-transform transform hover:scale-105"
        >
          Iniciar Sesión
        </button>
        <button
          onClick={() => navigate("/register")}
          className="bg-green-600 hover:bg-green-700 text-white py-2 px-4 rounded-lg text-sm shadow-lg transition-transform transform hover:scale-105"
        >
          Crear Cuenta
        </button>
      </div>

      {/* Hero Section */}
      <section className="relative h-screen flex items-center justify-center text-center bg-black">
        {/* Video Background */}
        <video
          className="absolute top-0 left-0 w-full h-full object-cover opacity-50"
          autoPlay
          muted
          loop
        >
          <source src="../videos/team_welcome.mp4" type="video/mp4" />
        </video>
        <div className="relative z-10 text-white px-4 flex flex-col items-center">
          <div className="flex items-center gap-4 mb-6">
            <img
              src="../images/echo_logo.png"
              alt="Jira Echo Logo"
              className="w-16 h-16 object-contain"
            />
            <h1 className="text-4xl font-bold">Jira Echo</h1>
          </div>
          <h2 className="text-5xl font-bold mb-4">Transforma tu forma de trabajar</h2>
          <p className="text-lg mb-6">
            Automatiza y gestiona tus proyectos con comandos de voz e inteligencia
            artificial.
          </p>
          <button
            onClick={() => navigate("/register")}
            className="bg-blue-600 hover:bg-blue-700 text-white py-3 px-6 rounded-lg text-lg shadow-lg transition-transform transform hover:scale-105"
          >
            Regístrate Ahora
          </button>
        </div>
      </section>


      {/* Features Section */}
      <section className="py-16 bg-white">
        <div className="max-w-6xl mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-8">
          {/* Feature Blocks */}
          <div className="text-center">
            <i className="fas fa-microphone-alt text-blue-600 text-5xl mb-4"></i>
            <h2 className="text-2xl font-semibold mb-2">Reconocimiento de Voz</h2>
            <p className="text-gray-600">
              Captura cada palabra con precisión y transcribe automáticamente tus reuniones.
            </p>
          </div>
          <div className="text-center">
            <i className="fas fa-tasks text-blue-600 text-5xl mb-4"></i>
            <h2 className="text-2xl font-semibold mb-2">Automatización</h2>
            <p className="text-gray-600">
              Conecta con Jira para gestionar proyectos y asignar tareas sin complicaciones.
            </p>
          </div>
          <div className="text-center">
            <i className="fas fa-chart-line text-blue-600 text-5xl mb-4"></i>
            <h2 className="text-2xl font-semibold mb-2">Seguimiento en Tiempo Real</h2>
            <p className="text-gray-600">
              Mantente al día con tus proyectos de Jira.
            </p>
          </div>
        </div>
      </section>

      {/* Call to Action Section */}
      <section className="py-16 bg-blue-600 text-white text-center">
        <h2 className="text-3xl font-bold mb-4">¿Listo para optimizar tu flujo de trabajo?</h2>
        <p className="mb-6 text-lg">
          Comienza hoy y descubre cómo nuestra plataforma puede transformar tu equipo.
        </p>
        <button
          onClick={() => navigate("/register")}
          className="bg-white text-blue-600 py-3 px-6 rounded-lg text-lg shadow-lg transition-transform transform hover:scale-105"
        >
          Crear Cuenta
        </button>
      </section>

      {/* Footer */}
      <Footer />
    </div>
  );
}

export default WelcomeScreen;
