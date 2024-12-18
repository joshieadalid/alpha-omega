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

// Función para obtener todos los usuarios usando la API REST de Jira Cloud
async function getUsers() {
  try {
    const baseUrl = `https://${domain}.atlassian.net`;

    const config = {
      method: "get",
      url: `${baseUrl}/rest/api/3/users/search`,
      headers: { "Content-Type": "application/json" },
      auth: auth,
      params: {
        maxResults: 50  // Número máximo de usuarios a devolver
      }
    };
    const response = await axios.request(config);
    return response.data;  // Devuelve los datos de los usuarios
  } catch (error) {
    console.error(
      "Error al obtener los usuarios:",
      error.response ? error.response.data.errors : error.message
    );
    throw error;  // Lanza el error para que pueda ser capturado por el código Python
  }
}

// Función para traducir el JSON de usuarios a un formato legible en español usando OpenAI
async function translateUsersToSpanish(users) {
  if (!users || users.length === 0) {
    console.error("No se encontraron usuarios para traducir.");
    return "No se encontraron usuarios para traducir.";
  }

  const userDescriptions = users.map(user => {
    return `ID del usuario: ${user.accountId}\nNombre del usuario: ${user.displayName}\nCorreo electrónico: ${user.emailAddress || "No disponible"}\n`;
  }).join("\n");

  const openaiData = {
    model: "gpt-3.5-turbo",
    messages: [
      {
        role: "system",
        content: "Eres un asistente que traduce y presenta la información de usuarios de manera legible en español."
      },
      {
        role: "user",
        content: `Traduce y muestra en formato legible la siguiente información de usuarios que sea humanos: \n\n${userDescriptions}`
      }
    ]
  };

  try {
    const response = await axios.post("https://api.openai.com/v1/chat/completions", openaiData, configHeadersOpenAI);
    const translatedText = response.data.choices[0].message.content;
    return translatedText;  // Devuelve el texto traducido
  } catch (error) {
    console.error("Error al traducir los usuarios con OpenAI:", error.response ? error.response.data : error.message);
    throw error;
  }
}

// Función que obtiene los usuarios recientes y los traduce al español
const getRecentUsers = async () => {
  try {
    const recentUsers = await getUsers();
    //console.log("Usuarios recientes obtenidos:", recentUsers);  // Verifica la salida de los usuarios obtenidos
    const translatedUsers = await translateUsersToSpanish(recentUsers);
    console.log(translatedUsers);  // Imprime la traducción en un formato legible
  } catch (error) {
    console.error("Error en getRecentUsers:", error.message);
  }
};

// Ejecutar getRecentUsers si el archivo es llamado directamente
if (require.main === module) {
  getRecentUsers();
} else {
  module.exports = { getUsers, getRecentUsers, translateUsersToSpanish };
}
