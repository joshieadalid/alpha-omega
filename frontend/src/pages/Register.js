import React, { useState } from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";

function Register() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");


  const handleRegister = async (e) => {
    e.preventDefault();
    setErrorMessage(""); // Resetea el mensaje de error al intentar registrar

    try {
      const response = await fetch("http://127.0.0.1:5000/api/register", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username: name, email, password }),
      });

      const data = await response.json();

      if (response.ok) {
        setSuccessMessage("Usuario registrado exitosamente");
        setErrorMessage("");

        setTimeout(() => {
          window.location.href = "/login"; // Redirigir a la pantalla de inicio de sesión
        }, 3000);
      } else {
        setErrorMessage(data.error || "Error al registrar usuario.");
        setSuccessMessage("");
      }
    } catch (error) {
      console.error("Error:", error);
      setErrorMessage("Ocurrió un error al conectar con el servidor.");
    }
  };

  return (
    <div className="bg-white min-h-screen flex flex-col">
      <Header />
      <main className="flex-1 flex flex-col items-center justify-center p-8 lg:ml-64">
        <div className="flex flex-col-reverse lg:flex-row w-full max-w-5xl items-center">
          {/* Parte izquierda: Título y logo */}
          <div className="w-full lg:w-1/2 text-center lg:text-left flex flex-col items-center lg:items-start">
            <div className="flex items-center gap-4">
              <img
                src="/images/Jira_logo.png"
                alt="Jira Logo"
                className="w-12 h-12 object-contain"
              />
              <h1 className="text-4xl lg:text-5xl font-bold text-blue-900">
                Jira Echo: Voice Management Assistant
              </h1>
            </div>
            <p className="text-gray-600 text-lg mt-4">
              Simplifica la gestión de proyectos con comandos de voz.
            </p>
          </div>

          {/* Parte derecha: Formulario de registro */}
          <div className="w-full lg:w-1/2 flex justify-center lg:justify-end mt-8 lg:mt-0">
            <div className="bg-gradient-to-br from-blue-600 to-blue-800 p-6 rounded-lg shadow-lg text-white w-full max-w-md">
              <h2 className="text-xl font-bold mb-4 text-center">Crear Cuenta</h2>
              <form className="space-y-4" onSubmit={handleRegister}>
                <div>
                  <label
                    htmlFor="name"
                    className="block text-sm font-medium text-gray-100 mb-1"
                  >
                    Nombre
                  </label>
                  <input
                    type="text"
                    id="name"
                    name="name"
                    placeholder="Ingresa tu nombre completo"
                    className="w-full px-3 py-2 bg-white text-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    value={name}
                    onChange={(e) => setName(e.target.value)}
                    required
                  />
                </div>
                <div>
                  <label
                    htmlFor="email"
                    className="block text-sm font-medium text-gray-100 mb-1"
                  >
                    Correo Electrónico
                  </label>
                  <input
                    type="email"
                    id="email"
                    name="email"
                    placeholder="Ingresa tu correo"
                    className="w-full px-3 py-2 bg-white text-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                  />
                </div>
                <div>
                  <label
                    htmlFor="password"
                    className="block text-sm font-medium text-gray-100 mb-1"
                  >
                    Contraseña
                  </label>
                  <input
                    type="password"
                    id="password"
                    name="password"
                    placeholder="Crea una contraseña"
                    className="w-full px-3 py-2 bg-white text-gray-800 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                  />
                </div>
                {successMessage && (
                  <p className="text-green-400 text-sm text-center">{successMessage}</p>
                )}
                {errorMessage && (
                  <p className="text-red-400 text-sm text-center">{errorMessage}</p>
                )}
                <button
                  type="submit"
                  className="w-full bg-white text-blue-800 py-2 px-4 rounded-lg font-semibold hover:bg-gray-100 hover:scale-105 transition-transform duration-200"
                >
                  Crear Cuenta
                </button>
              </form>
              <div className="mt-4 text-center">
                <p className="text-sm">
                  ¿Ya tienes una cuenta?{" "}
                  <a href="/login" className="text-blue-300 hover:underline">
                    Iniciar Sesión
                  </a>
                </p>
              </div>
            </div>
          </div>
        </div>
      </main>
      <Footer />
    </div>
  );
}

export default Register;
