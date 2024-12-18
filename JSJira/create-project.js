const axios = require('axios');
require('dotenv').config();

const username = process.env.ATLASSIAN_USERNAME;
const password = process.env.ATLASSIAN_API_KEY;
const openaiApiKey = process.env.API_KEY_OPENAI;
const domain = process.env.DOMAIN;

// Mensaje del usuario y parámetros iniciales para el proyecto
const userMessage = process.argv[2] || "Genera un proyecto de prueba en Jira";       
const leadAccountID = "712020:bbd0967a-856f-4e09-be5a-13b51c668f38";  

// Configuración de autorización para Jira
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

// Llama a OpenAI para generar el JSON de creación de proyecto
async function generateProjectJSON() {
    const openaiData = {
        model: "gpt-3.5-turbo",
        messages: [
            {
                role: "system",
                content: "Eres un asistente que genera JSON para crear proyectos en Jira."
            },
            {
                role: "user",
                content: `Genera un JSON para crear un proyecto en Jira con la información de: ${userMessage} "Recuerda que leadAccountID es ${leadAccountID}"
                - name: 
                - key: 
                - leadAccountId: 
                - projectTypeKey: 'software'
                - projectTemplateKey: 'com.pyxis.greenhopper.jira:gh-simplified-scrum-classic'
                - assigneeType: 'PROJECT_LEAD'`
            }
        ]
    };

    try {
        const response = await axios.post("https://api.openai.com/v1/chat/completions", openaiData, configHeadersOpenAI);
        const jsonResponse = response.data.choices[0].message.content;
        console.log("JSON generado por OpenAI:", jsonResponse);

        // Convierte el JSON generado en un objeto
        return JSON.parse(jsonResponse);
    } catch (error) {
        console.error("Error al generar JSON con OpenAI:", error.response ? error.response.data : error.message);
        throw error;
    }
}

// Función para crear proyecto en Jira usando el JSON generado
async function createProjectInJira(projectData) {
    const baseUrl = `https://${domain}.atlassian.net`;
    const url = `${baseUrl}/rest/api/3/project`;

    try {
        const response = await axios.post(url, projectData, configHeadersJira);
        console.log("Proyecto creado en Jira:", response.data);
        return response.data.key;
    } catch (error) {
        console.error("Error al crear el proyecto en Jira:", error.response ? error.response.data : error.message);
    }
}

// Función principal
const createProjectA = async () => {
    try {
        const projectData = await generateProjectJSON();  // Genera JSON usando OpenAI
        const projectKey = await createProjectInJira(projectData);  // Crea el proyecto en Jira
        console.log(`Created project with key: ${projectKey}`);
    } catch (error) {
        console.error("Error en la creación del proyecto:", error);
    }
};

// Ejecuta la función principal si el archivo es llamado directamente
if (require.main === module) {
    createProjectA();
} else {
    module.exports = { createProjectA };
}
