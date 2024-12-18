const axios = require("axios");
require("dotenv").config();

const username = process.env.ATLASSIAN_USERNAME;
const password = process.env.ATLASSIAN_API_KEY;
const domain = process.env.DOMAIN;
const openaiApiKey = process.env.API_KEY_OPENAI;

const userMessage =
  process.argv[2] || "Eliminar el proyecto con ID 10001 en Jira"; // Ejemplo de mensaje del usuario

const configHeadersOpenAI = {
  headers: {
    Authorization: `Bearer ${openaiApiKey}`,
    "Content-Type": "application/json",
  },
};

// Llama a OpenAI para extraer solo el ID del proyecto del mensaje del usuario
async function extractProjectId(message) {
  const openaiData = {
    model: "gpt-3.5-turbo",
    messages: [
      {
        role: "system",
        content:
          "Eres un asistente que extrae el ID del proyecto de mensajes para eliminarlo en Jira. Solo devuelve el ID, sin texto adicional.",
      },
      {
        role: "user",
        content: `Extrae el ID del proyecto del siguiente mensaje: "${message}"`,
      },
    ],
  };

  try {
    const response = await axios.post(
      "https://api.openai.com/v1/chat/completions",
      openaiData,
      configHeadersOpenAI,
    );
    const extractedId = response.data.choices[0].message.content.trim(); // Se asume que OpenAI devuelve solo el ID
    console.log("ID del proyecto extraído:", extractedId);
    return extractedId;
  } catch (error) {
    console.error(
      "Error al extraer el ID del proyecto con OpenAI:",
      error.response ? error.response.data : error.message,
    );
    throw error;
  }
}

// Función para eliminar un proyecto mediante su ID en Jira
async function deleteProject(projectId) {
  try {
    const baseUrl = `https://${domain}.atlassian.net`;

    const config = {
      method: "delete",
      url: `${baseUrl}/rest/api/3/project/${projectId}`,
      headers: { "Content-Type": "application/json" },
      auth: {
        username: username,
        password: password,
      },
    };

    const response = await axios.request(config);
    console.log(`Proyecto con ID ${projectId} eliminado exitosamente.`);
    return response.data;
  } catch (error) {
    console.log("Error al eliminar el proyecto:");
    console.log(error.response ? error.response.data : error.message);
  }
}

// Función principal que extrae el ID del proyecto y lo elimina
const deleteProjectA = async () => {
  try {
    const projectId = await extractProjectId(userMessage); // Extrae el ID usando OpenAI
    if (projectId) {
      await deleteProject(projectId); // Elimina el proyecto si se extrajo correctamente el ID
    } else {
      console.error(
        "No se pudo extraer el ID del proyecto del mensaje proporcionado.",
      );
    }
  } catch (error) {
    console.error("Error en el proceso de eliminación del proyecto:", error);
  }
};

// Ejecutar deleteProjectA si el archivo es llamado directamente
if (require.main === module) {
  deleteProjectA();
} else {
  module.exports = { deleteProject, deleteProjectA }; // Exportar ambas funciones
}
