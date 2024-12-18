const axios = require("axios");
require("dotenv").config();

const username = process.env.ATLASSIAN_USERNAME;
const password = process.env.ATLASSIAN_API_KEY;
const domain = process.env.DOMAIN;

const auth = {
  username: username,
  password: password,
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
    return response.data;
  } catch (error) {
    console.error(
      "Error al obtener los proyectos:",
      error.response ? error.response.data.errors : error.message,
    );
  }
}

// Función que llama a getProjects y muestra solo los nombres de los proyectos recientes
const getRecentProjects = async () => {
  const recentProjects = await getProjects();
  if (recentProjects) {
    const projectNames = recentProjects.map((project) => project.name);
    console.log("Nombres de los proyectos recientes:");
    projectNames.forEach((name) => console.log(name));
  }
};

// Ejecutar getRecentProjects si el archivo es llamado directamente
if (require.main === module) {
  getRecentProjects();
} else {
  module.exports = { getProjects, getRecentProjects }; // Exportar ambas funciones
}
