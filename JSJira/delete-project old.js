const axios = require('axios');
require('dotenv').config();

const username = process.env.ATLASSIAN_USERNAME;
const password = process.env.ATLASSIAN_API_KEY;
const domain = process.env.DOMAIN;
const openaiApiKey = process.env.API_KEY_OPENAI;

const userMessage = process.argv[2] || "Genera un proyecto de prueba en Jira";      

const auth = Buffer.from(`${username}:${password}`).toString('base64');
const configHeadersJira = {
    headers: {
        'Authorization': `Basic ${auth}`,
        'Content-Type': 'application/json',
    }
};

// Configuración de autorización para OpenAI
const configHeadersOpenAI = {
    headers: {
        'Authorization': `Bearer ${openaiApiKey}`,
        'Content-Type': 'application/json',
    }
};

// Función para eliminar un proyecto mediante su ID
async function deleteProject(projectId) {
  try {
    const baseUrl = `https://${domain}.atlassian.net`;

    const config = {
      method: 'delete',
      url: `${baseUrl}/rest/api/3/project/${projectId}`,
      headers: { 'Content-Type': 'application/json' },
      auth: auth
    };

    const response = await axios.request(config);
    console.log(`Proyecto con ID ${projectId} eliminado exitosamente.`);
    return response.data;
  } catch (error) {
    console.log('Error al eliminar el proyecto:');
    console.log(error.response ? error.response.data : error.message);
  }
}

// Función que llama a deleteProject para eliminar un proyecto con un ID específico
const deleteProjectA = async () => {
  const projectId = '10001'; // Reemplaza con el ID del proyecto que deseas eliminar
  await deleteProject(projectId);
};

// Ejecutar deleteProjectA si el archivo es llamado directamente
if (require.main === module) {
  deleteProjectA();
} else {
  module.exports = { deleteProject, deleteProjectA };  // Exportar ambas funciones
}
