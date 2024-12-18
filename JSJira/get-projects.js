const axios = require("axios");
require("dotenv").config();

const username = process.env.ATLASSIAN_USERNAME;
const password = process.env.ATLASSIAN_API_KEY;
const domain = process.env.DOMAIN;
const openaiApiKey = process.env.API_KEY_OPENAI;

const auth = {
  username: username,
  password: password,
};

// Configuración de autorización para OpenAI
const configHeadersOpenAI = {
  headers: {
    'Authorization': `Bearer ${openaiApiKey}`,
    'Content-Type': 'application/json',
  }
};

// Función para obtener todos los proyectos recientes usando la API REST de Jira Cloud
async function getProjects() {
  try {
    const baseUrl = `https://${domain}.atlassian.net`;

    const config = {
      method: "get",
      url: `${baseUrl}/rest/api/3/project`,
      headers: { "Content-Type": "application/json" },
      auth: auth,
    };
    const response = await axios.request(config);
    return response.data;  // Devuelve los datos de los proyectos
  } catch (error) {
    console.error(
      "Error al obtener los proyectos:",
      error.response ? error.response.data.errors : error.message
    );
    throw error;  // Lanza el error para que pueda ser capturado por el código Python
  }
}

// Función para traducir el JSON de proyectos a un formato legible en español usando OpenAI
async function translateProjectsToSpanish(projects) {
  if (!projects || projects.length === 0) {
    console.error("No se encontraron proyectos para traducir.");
    return "No se encontraron proyectos para traducir.";
  }

  const projectDescriptions = projects.map(project => {
    return `ID del proyecto: ${project.id}\nNombre del proyecto: ${project.name}\nDescripción: ${project.description || "Sin descripción"}\nClave del proyecto: ${project.key}\n`;
  }).join("\n");

  const openaiData = {
    model: "gpt-3.5-turbo",
    messages: [
      {
        role: "system",
        content: "Eres un asistente que traduce y presenta la información de proyectos de manera legible en español."
      },
      {
        role: "user",
        content: `Traduce y muestra en formato legible la siguiente información de proyectos:\n\n${projectDescriptions}`
      }
    ]
  };

  try {
    const response = await axios.post("https://api.openai.com/v1/chat/completions", openaiData, configHeadersOpenAI);
    const translatedText = response.data.choices[0].message.content;
    return translatedText;  // Devuelve el texto traducido
  } catch (error) {
    console.error("Error al traducir los proyectos con OpenAI:", error.response ? error.response.data : error.message);
    throw error;
  }
}

// Función que obtiene los proyectos recientes y los traduce al español
const getRecentProjects = async () => {
  try {
    const recentProjects = await getProjects();
    //console.log("Proyectos recientes obtenidos:", recentProjects);  // Verifica la salida de los proyectos obtenidos
    const translatedProjects = await translateProjectsToSpanish(recentProjects);
    console.log(translatedProjects);  // Imprime la traducción en un formato legible
  } catch (error) {
    console.error("Error en getRecentProjects:", error.message);
  }
};

// Ejecutar getRecentProjects si el archivo es llamado directamente
if (require.main === module) {
  getRecentProjects();
} else {
  module.exports = { getProjects, getRecentProjects, translateProjectsToSpanish };
}
