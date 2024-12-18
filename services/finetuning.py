trainingData = [
    # Crear proyectos de alta prioridad
    # Crear proyectos de alta prioridad en Jira
    { "prompt": "Crear un proyecto urgente para mejorar el rendimiento del servidor en Jira", "completion": "createProject({name: 'Mejora de Rendimiento del Servidor', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Generar un proyecto de alta prioridad para reforzar la seguridad de los datos de clientes en Jira", "completion": "createProject({name: 'Refuerzo de Seguridad de Datos', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Iniciar un proyecto en Jira para revisar la infraestructura de redes y optimizar el tráfico", "completion": "createProject({name: 'Revisión de Infraestructura de Redes', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Crear un proyecto crítico en Jira para implementar un plan de recuperación de desastres", "completion": "createProject({name: 'Plan de Recuperación de Desastres', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Lanzar un proyecto de alta prioridad en Jira para actualizar el sistema de respaldo de datos", "completion": "createProject({name: 'Actualización del Sistema de Respaldo de Datos', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Iniciar un proyecto de alta prioridad en Jira para implementar políticas de autenticación multifactor", "completion": "createProject({name: 'Autenticación Multifactor', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Crear un proyecto urgente en Jira para actualizar el sistema de monitoreo de red", "completion": "createProject({name: 'Actualización de Monitoreo de Red', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Generar un proyecto de alta prioridad en Jira para mejorar la gestión de accesos a datos sensibles", "completion": "createProject({name: 'Gestión de Accesos a Datos Sensibles', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Iniciar un proyecto en Jira para desarrollar un sistema de alerta temprana ante incidentes de seguridad", "completion": "createProject({name: 'Sistema de Alerta Temprana de Seguridad', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Crear un proyecto de alta prioridad en Jira para optimizar el flujo de trabajo de los equipos", "completion": "createProject({name: 'Optimización del Flujo de Trabajo', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Lanzar un proyecto crítico en Jira para mejorar la protección de redes contra ataques DDoS", "completion": "createProject({name: 'Protección contra Ataques DDoS', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Generar un proyecto de alta prioridad en Jira para implementar un sistema de control de versiones de software", "completion": "createProject({name: 'Control de Versiones de Software', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Crear un proyecto urgente en Jira para fortalecer la encriptación de datos sensibles", "completion": "createProject({name: 'Fortalecimiento de Encriptación de Datos', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Iniciar un proyecto en Jira para desarrollar un sistema de auditoría de accesos a sistemas", "completion": "createProject({name: 'Sistema de Auditoría de Accesos', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Crear un proyecto de alta prioridad en Jira para realizar una auditoría completa de ciberseguridad", "completion": "createProject({name: 'Auditoría Completa de Ciberseguridad', priority: 'Alta', platform: 'Jira'})" },
    { "prompt": "Crear un proyecto urgente para mejorar la infraestructura de redes en la empresa", "completion": "createProject({name: 'Mejora de Infraestructura de Redes', priority: 'Alta'})" },
    { "prompt": "Iniciar un proyecto de análisis de riesgos en ciberseguridad con prioridad alta", "completion": "createProject({name: 'Análisis de Riesgos en Ciberseguridad', priority: 'Alta'})" },
    { "prompt": "Crear un proyecto de investigación sobre machine learning para optimización de recursos", "completion": "createProject({name: 'Investigación de Machine Learning para Optimización', priority: 'Alta'})" },
    { "prompt": "Generar un proyecto crítico para actualizar la base de datos de clientes antes de fin de año", "completion": "createProject({name: 'Actualización de Base de Datos de Clientes', priority: 'Alta'})" },
    { "prompt": "Crear un proyecto de alta prioridad para implementar mejoras en la eficiencia energética", "completion": "createProject({name: 'Mejoras en Eficiencia Energética', priority: 'Alta'})" },

    # Actualización urgente de proyectos
    { "prompt": "Actualizar el proyecto 'Optimización de Recursos' para agregar una nueva fecha límite el 20 de febrero", "completion": "updateProject({name: 'Optimización de Recursos', dueDate: '2025-02-20'})" },
    { "prompt": "Modificar el proyecto 'Expansión de Mercados' para incluir un análisis de competencia en el sprint 4", "completion": "updateProject({name: 'Expansión de Mercados', phase: 4, addTask: 'Análisis de Competencia'})" },
    { "prompt": "Actualizamos el proyecto 'Desarrollo de Producto' para añadir una fase de pruebas piloto", "completion": "updateProject({name: 'Desarrollo de Producto', addPhase: 'Pruebas Piloto'})" },
    { "prompt": "Modificar el proyecto 'Evaluación de Proveedores' para añadir un especialista en logística en el equipo", "completion": "updateProject({name: 'Evaluación de Proveedores', addTeam: 'Especialista en Logística'})" },
    { "prompt": "Actualización del proyecto 'Campaña Publicitaria' para ajustar la fecha de inicio al 1 de marzo", "completion": "updateProject({name: 'Campaña Publicitaria', startDate: '2025-03-01'})" },
    { "prompt": "Modificamos el proyecto 'Rediseño de Marca' para añadir revisión de branding en el sprint 2", "completion": "updateProject({name: 'Rediseño de Marca', phase: 2, addTask: 'Revisión de Branding'})" },
    { "prompt": "Actualizar el proyecto 'Automatización de Procesos' para incluir una revisión de calidad en la fase final", "completion": "updateProject({name: 'Automatización de Procesos', addPhase: 'Revisión de Calidad'})" },
    { "prompt": "Modificar el proyecto 'Optimización del Servicio al Cliente' para ajustar la fecha de entrega al 30 de abril", "completion": "updateProject({name: 'Optimización del Servicio al Cliente', dueDate: '2025-04-30'})" },
    { "prompt": "Actualizamos el proyecto 'Integración de Sistemas' para añadir soporte de TI en el sprint 1", "completion": "updateProject({name: 'Integración de Sistemas', phase: 1, addTeam: 'Soporte de TI'})" },
    { "prompt": "Actualizar el proyecto 'Capacitación Interna' para añadir una nueva fase de evaluación al final", "completion": "updateProject({name: 'Capacitación Interna', addPhase: 'Evaluación Final'})" },
    { "prompt": "Modificar el proyecto 'Expansión Internacional' para incluir una revisión legal en el sprint 3", "completion": "updateProject({name: 'Expansión Internacional', phase: 3, addTask: 'Revisión Legal'})" },
    { "prompt": "Actualización del proyecto 'Estrategia de Ventas' para agregar un equipo de consultoría de mercado", "completion": "updateProject({name: 'Estrategia de Ventas', addTeam: 'Consultoría de Mercado'})" },
    { "prompt": "Modificamos el proyecto 'Desarrollo de Software' para añadir revisión de código en el sprint 5", "completion": "updateProject({name: 'Desarrollo de Software', phase: 5, addTask: 'Revisión de Código'})" },
    { "prompt": "Actualizar el proyecto 'Servicio Postventa' para ajustar la fecha límite al 15 de mayo", "completion": "updateProject({name: 'Servicio Postventa', dueDate: '2025-05-15'})" },
    { "prompt": "Modificamos el proyecto 'Estudio de Mercado' para añadir un equipo de análisis en el sprint 2", "completion": "updateProject({name: 'Estudio de Mercado', phase: 2, addTeam: 'Equipo de Análisis'})" },
    { "prompt": "Actualizar el proyecto 'Optimización de Procesos' para agregar una nueva fecha límite de entrega para el 15 de enero", "completion": "updateProject({name: 'Optimización de Procesos', dueDate: '2025-01-15'})" },
    { "prompt": "Actualizar el proyecto 'Automatización de Marketing' para incluir a un especialista en análisis de datos en la fase inicial", "completion": "updateProject({name: 'Automatización de Marketing', phase: 1, addTeam: 'Especialista en Análisis de Datos'})" },
    { "prompt": "Modificar el proyecto 'Desarrollo de App Móvil' para incluir una revisión de usabilidad en la fase 3", "completion": "updateProject({name: 'Desarrollo de App Móvil', phase: 3, addTeam: 'Equipo de Usabilidad'})" },
    { "prompt": "Actualizar el proyecto 'Implementación ERP' para agregar una nueva fase de capacitación al personal", "completion": "updateProject({name: 'Implementación ERP', addPhase: 'Capacitación'})" },
    { "prompt": "Modificar el proyecto 'Rediseño Web' para incluir un equipo de diseño gráfico en la fase 2", "completion": "updateProject({name: 'Rediseño Web', phase: 2, addTeam: 'Equipo de Diseño Gráfico'})" },

    # Asignar tareas importantes y urgentes
    { "prompt": "Encargar la tarea 'Revisión de especificaciones técnicas' a De La Cruz Gonzalez Axel Adolfo en el proyecto 'Innovación Tecnológica'", "completion": "assignTask({project: 'Innovación Tecnológica', task: 'Revisión de especificaciones técnicas', assignee: 'De La Cruz Gonzalez Axel Adolfo'})" },
    { "prompt": "Responsabilizar a Escobar Montoya Patricio de la tarea 'Generar reportes de ventas' en el proyecto 'Expansión Comercial'", "completion": "assignTask({project: 'Expansión Comercial', task: 'Generar reportes de ventas', assignee: 'Escobar Montoya Patricio'})" },
    { "prompt": "Designar la tarea 'Planificar campaña de redes sociales' a Juarez Botello Josué Adalid en el proyecto 'Marketing Digital'", "completion": "assignTask({project: 'Marketing Digital', task: 'Planificar campaña de redes sociales', assignee: 'Juarez Botello Josué Adalid'})" },
    { "prompt": "Encargar la tarea 'Desarrollar base de datos de clientes' a Juarez Solano Juan Martín en el proyecto 'Gestión de Clientes'", "completion": "assignTask({project: 'Gestión de Clientes', task: 'Desarrollar base de datos de clientes', assignee: 'Juarez Solano Juan Martín'})" },
    { "prompt": "Responsabilizar a Martinez Serrano Alexis Geovanni de la tarea 'Revisar políticas de seguridad' en el proyecto 'Cumplimiento TI'", "completion": "assignTask({project: 'Cumplimiento TI', task: 'Revisar políticas de seguridad', assignee: 'Martinez Serrano Alexis Geovanni'})" },
    { "prompt": "Designar la tarea 'Preparar informe anual' a Montoya Gutierrez Pavel en el proyecto 'Reporte Financiero'", "completion": "assignTask({project: 'Reporte Financiero', task: 'Preparar informe anual', assignee: 'Montoya Gutierrez Pavel'})" },
    { "prompt": "Encargar la tarea 'Optimización de recursos' a Rodriguez Cuellar Spencer Fabian en el proyecto 'Recursos Humanos'", "completion": "assignTask({project: 'Recursos Humanos', task: 'Optimización de recursos', assignee: 'Rodriguez Cuellar Spencer Fabian'})" },
    { "prompt": "Responsabilizar a Sireno Ojeda Cesar Abraham de la tarea 'Auditoría de sistemas' en el proyecto 'Control Interno'", "completion": "assignTask({project: 'Control Interno', task: 'Auditoría de sistemas', assignee: 'Sireno Ojeda Cesar Abraham'})" },
    { "prompt": "Designar la tarea 'Desarrollar plan de capacitación' a De La Cruz Gonzalez, Axel Adolfo en el proyecto 'Recursos Humanos'", "completion": "assignTask({project: 'Recursos Humanos', task: 'Desarrollar plan de capacitación', assignee: 'De La Cruz Gonzalez, Axel Adolfo'})" },
    { "prompt": "Encargar la tarea 'Realizar encuestas de satisfacción' a Escobar Montoya, Patricio en el proyecto 'Calidad de Servicio'", "completion": "assignTask({project: 'Calidad de Servicio', task: 'Realizar encuestas de satisfacción', assignee: 'Escobar Montoya, Patricio'})" },
    { "prompt": "Responsabilizar a Juarez Botello, Josué Adalid de la tarea 'Actualizar inventario de hardware' en el proyecto 'Gestión de Activos'", "completion": "assignTask({project: 'Gestión de Activos', task: 'Actualizar inventario de hardware', assignee: 'Juarez Botello, Josué Adalid'})" },
    { "prompt": "Encargar la tarea 'Realizar pruebas de funcionalidad' a Juarez Solano, Juan Martín en el proyecto 'Pruebas de Producto'", "completion": "assignTask({project: 'Pruebas de Producto', task: 'Realizar pruebas de funcionalidad', assignee: 'Juarez Solano, Juan Martín'})" },
    { "prompt": "Designar la tarea 'Auditar cuentas contables' a Martinez Serrano, Alexis Geovanni en el proyecto 'Revisión Contable'", "completion": "assignTask({project: 'Revisión Contable', task: 'Auditar cuentas contables', assignee: 'Martinez Serrano, Alexis Geovanni'})" },
    { "prompt": "Responsabilizar a Montoya Gutierrez, Pavel de la tarea 'Revisión de contratos' en el proyecto 'Cumplimiento Legal'", "completion": "assignTask({project: 'Cumplimiento Legal', task: 'Revisión de contratos', assignee: 'Montoya Gutierrez, Pavel'})" },
    { "prompt": "Encargar la tarea 'Optimización de procesos' a Rodriguez Cuellar, Spencer Fabian en el proyecto 'Eficiencia Operativa'", "completion": "assignTask({project: 'Eficiencia Operativa', task: 'Optimización de procesos', assignee: 'Rodriguez Cuellar, Spencer Fabian'})" },
    { "prompt": "Designar la tarea 'Actualización de sistemas de seguridad' a Sireno Ojeda, Cesar Abraham en el proyecto 'Infraestructura TI'", "completion": "assignTask({project: 'Infraestructura TI', task: 'Actualización de sistemas de seguridad', assignee: 'Sireno Ojeda, Cesar Abraham'})" },
    { "prompt": "Responsabilizar a Axel Adolfo de la tarea 'Planificación de recursos' en el proyecto 'Infraestructura Corporativa'", "completion": "assignTask({project: 'Infraestructura Corporativa', task: 'Planificación de recursos', assignee: 'Axel Adolfo De La Cruz Gonzalez'})" },
    { "prompt": "Encargar la tarea 'Supervisión de ventas mensuales' a Patricio en el proyecto 'Gestión Comercial'", "completion": "assignTask({project: 'Gestión Comercial', task: 'Supervisión de ventas mensuales', assignee: 'Patricio Escobar Montoya'})" },
    { "prompt": "Designar la tarea 'Análisis de mercado' a Josué Adalid en el proyecto 'Estrategia de Mercado'", "completion": "assignTask({project: 'Estrategia de Mercado', task: 'Análisis de mercado', assignee: 'Josué Adalid Juarez Botello'})" },
    { "prompt": "Responsabilizar a Juan Martín de la tarea 'Evaluación de rendimiento' en el proyecto 'Recursos Humanos'", "completion": "assignTask({project: 'Recursos Humanos', task: 'Evaluación de rendimiento', assignee: 'Juan Martín Juarez Solano'})" },
    { "prompt": "Encargar la tarea 'Coordinación de logística de eventos' a Alexis Geovanni en el proyecto 'Relaciones Públicas'", "completion": "assignTask({project: 'Relaciones Públicas', task: 'Coordinación de logística de eventos', assignee: 'Alexis Geovanni Martinez Serrano'})" },
    { "prompt": "Designar la tarea 'Revisión de arquitectura de red' a Pavel en el proyecto 'Infraestructura IT'", "completion": "assignTask({project: 'Infraestructura IT', task: 'Revisión de arquitectura de red', assignee: 'Pavel Montoya Gutierrez'})" },
    { "prompt": "Responsabilizar a Spencer Fabian de la tarea 'Evaluación de proveedores' en el proyecto 'Suministros Corporativos'", "completion": "assignTask({project: 'Suministros Corporativos', task: 'Evaluación de proveedores', assignee: 'Spencer Fabian Rodriguez Cuellar'})" },
    { "prompt": "Encargar la tarea 'Planificación de auditoría interna' a Cesar Abraham en el proyecto 'Cumplimiento Normativo'", "completion": "assignTask({project: 'Cumplimiento Normativo', task: 'Planificación de auditoría interna', assignee: 'Cesar Abraham Sireno Ojeda'})" },

    # Cambiar el estado de tareas en proyectos críticos
    { "prompt": "Cambiar el estado de la tarea 'Desarrollar sistema de autenticación' en el proyecto 'Seguridad' a 'En progreso'", "completion": "updateTaskStatus({project: 'Seguridad', task: 'Desarrollar sistema de autenticación', status: 'En progreso'})" },
    { "prompt": "Marcar la tarea 'Analizar requisitos de cliente' como 'Completada' en el proyecto 'Desarrollo de Software'", "completion": "updateTaskStatus({project: 'Desarrollo de Software', task: 'Analizar requisitos de cliente', status: 'Completada'})" },
    { "prompt": "Actualizar el estado de la tarea 'Crear prototipo de interfaz' en el proyecto 'UX/UI' a 'Pendiente'", "completion": "updateTaskStatus({project: 'UX/UI', task: 'Crear prototipo de interfaz', status: 'Pendiente'})" },
    { "prompt": "Cambiar el estado de la tarea 'Instalar sistema de control de calidad' en el proyecto 'Control de Calidad' a 'En revisión'", "completion": "updateTaskStatus({project: 'Control de Calidad', task: 'Instalar sistema de control de calidad', status: 'En revisión'})" },
    { "prompt": "Marcar la tarea 'Elaborar reporte de incidentes' como 'En progreso' en el proyecto 'Seguridad TI'", "completion": "updateTaskStatus({project: 'Seguridad TI', task: 'Elaborar reporte de incidentes', status: 'En progreso'})" },
    { "prompt": "Cambiar el estado de la tarea 'Desarrollar aplicación móvil' en el proyecto 'Aplicaciones' a 'En progreso'", "completion": "updateTaskStatus({project: 'Aplicaciones', task: 'Desarrollar aplicación móvil', status: 'En progreso'})" },
    { "prompt": "Marcar la tarea 'Revisar código de integración' como 'Pendiente' en el proyecto 'Desarrollo de Software'", "completion": "updateTaskStatus({project: 'Desarrollo de Software', task: 'Revisar código de integración', status: 'Pendiente'})" },
    { "prompt": "Actualizar el estado de la tarea 'Realizar pruebas de seguridad' en el proyecto 'Seguridad Web' a 'Completada'", "completion": "updateTaskStatus({project: 'Seguridad Web', task: 'Realizar pruebas de seguridad', status: 'Completada'})" },
    { "prompt": "Cambiar el estado de la tarea 'Revisar diseño de arquitectura' en el proyecto 'Infraestructura TI' a 'En revisión'", "completion": "updateTaskStatus({project: 'Infraestructura TI', task: 'Revisar diseño de arquitectura', status: 'En revisión'})" },
    { "prompt": "Marcar la tarea 'Implementar mejoras de rendimiento' como 'En progreso' en el proyecto 'Optimización de Sistemas'", "completion": "updateTaskStatus({project: 'Optimización de Sistemas', task: 'Implementar mejoras de rendimiento', status: 'En progreso'})" },
    { "prompt": "Actualizar el estado de la tarea 'Crear documentación técnica' en el proyecto 'Documentación' a 'Pendiente'", "completion": "updateTaskStatus({project: 'Documentación', task: 'Crear documentación técnica', status: 'Pendiente'})" },
    { "prompt": "Cambiar el estado de la tarea 'Optimizar algoritmo de búsqueda' en el proyecto 'Desarrollo de Software' a 'En progreso'", "completion": "updateTaskStatus({project: 'Desarrollo de Software', task: 'Optimizar algoritmo de búsqueda', status: 'En progreso'})" },
    { "prompt": "Marcar la tarea 'Revisar experiencia de usuario' como 'Completada' en el proyecto 'UX/UI'", "completion": "updateTaskStatus({project: 'UX/UI', task: 'Revisar experiencia de usuario', status: 'Completada'})" },
    { "prompt": "Actualizar el estado de la tarea 'Verificar compatibilidad de software' en el proyecto 'Control de Calidad' a 'En revisión'", "completion": "updateTaskStatus({project: 'Control de Calidad', task: 'Verificar compatibilidad de software', status: 'En revisión'})" },
    { "prompt": "Cambiar el estado de la tarea 'Actualizar sistema de base de datos' en el proyecto 'Infraestructura' a 'En progreso'", "completion": "updateTaskStatus({project: 'Infraestructura', task: 'Actualizar sistema de base de datos', status: 'En progreso'})" },
    { "prompt": "Marcar la tarea 'Desarrollar pruebas unitarias' como 'Pendiente' en el proyecto 'Automatización'", "completion": "updateTaskStatus({project: 'Automatización', task: 'Desarrollar pruebas unitarias', status: 'Pendiente'})" },
    { "prompt": "Actualizar el estado de la tarea 'Analizar datos de rendimiento' en el proyecto 'Optimización' a 'Completada'", "completion": "updateTaskStatus({project: 'Optimización', task: 'Analizar datos de rendimiento', status: 'Completada'})" },
    { "prompt": "Cambiar el estado de la tarea 'Elaborar informe de resultados' en el proyecto 'Investigación' a 'En progreso'", "completion": "updateTaskStatus({project: 'Investigación', task: 'Elaborar informe de resultados', status: 'En progreso'})" },
    { "prompt": "Marcar la tarea 'Desarrollar estrategia de ventas' como 'En revisión' en el proyecto 'Estrategia Comercial'", "completion": "updateTaskStatus({project: 'Estrategia Comercial', task: 'Desarrollar estrategia de ventas', status: 'En revisión'})" },
    { "prompt": "Actualizar el estado de la tarea 'Implementar sistema de feedback' en el proyecto 'Plataforma Web' a 'Pendiente'", "completion": "updateTaskStatus({project: 'Plataforma Web', task: 'Implementar sistema de feedback', status: 'Pendiente'})" },

    # Definir reuniones estratégicas con fechas y objetivos claros
    { "prompt": "Crear una reunión estratégica para revisar el proyecto 'Desarrollo de Software' el 12 de diciembre a las 2 PM", "completion": "createMeeting({project: 'Desarrollo de Software', date: '2024-12-12', time: '14:00', objective: 'Revisión de avances y planificación'})" },
    { "prompt": "Crear una reunión de equipo para discutir el proyecto 'Transformación Digital' el 15 de noviembre a las 9 AM", "completion": "createMeeting({project: 'Transformación Digital', date: '2024-11-15', time: '09:00', objective: 'Evaluación del progreso y ajustes'})" },
    { "prompt": "Agendar una reunión de planificación para el proyecto 'Desarrollo de Software' el 12 de diciembre a las 2 PM", "completion": "createMeeting({project: 'Desarrollo de Software', date: '2024-12-12', time: '14:00', objective: 'Revisión de avances y planificación'})" },
    { "prompt": "Convocar una reunión de seguimiento para el proyecto 'Transformación Digital' el 15 de noviembre a las 9 AM", "completion": "createMeeting({project: 'Transformación Digital', date: '2024-11-15', time: '09:00', objective: 'Evaluación del progreso y ajustes'})" },
    { "prompt": "Establecer una reunión de revisión para el proyecto 'Automatización de Marketing' el 20 de noviembre a las 11 AM", "completion": "createMeeting({project: 'Automatización de Marketing', date: '2024-11-20', time: '11:00', objective: 'Revisión de métricas y resultados'})" },
    { "prompt": "Coordinar una reunión ejecutiva para discutir el proyecto 'Mejora de Infraestructura' el 5 de diciembre a las 4 PM", "completion": "createMeeting({project: 'Mejora de Infraestructura', date: '2024-12-05', time: '16:00', objective: 'Análisis de avance y decisiones estratégicas'})" },
    { "prompt": "Fijar una reunión de planificación para el proyecto 'Reestructuración Organizacional' el 2 de diciembre a las 10 AM", "completion": "createMeeting({project: 'Reestructuración Organizacional', date: '2024-12-02', time: '10:00', objective: 'Planificación de tareas y asignaciones'})" },
    { "prompt": "Proponer una reunión de alineación estratégica para el proyecto 'Innovación de Producto' el 8 de diciembre a las 3 PM", "completion": "createMeeting({project: 'Innovación de Producto', date: '2024-12-08', time: '15:00', objective: 'Alineación de objetivos y recursos'})" },
    { "prompt": "Solicitar una reunión de actualización para el proyecto 'Expansión Internacional' el 10 de diciembre a las 12 PM", "completion": "createMeeting({project: 'Expansión Internacional', date: '2024-12-10', time: '12:00', objective: 'Evaluación de avances y desafíos'})" },
    { "prompt": "Programar una reunión de toma de decisiones para el proyecto 'Transformación Digital' el 16 de noviembre a las 2 PM", "completion": "createMeeting({project: 'Transformación Digital', date: '2024-11-16', time: '14:00', objective: 'Toma de decisiones clave y asignación de responsabilidades'})" },
    { "prompt": "Definir una reunión de estrategia para el proyecto 'Optimización de Procesos' el 18 de noviembre a las 4 PM", "completion": "createMeeting({project: 'Optimización de Procesos', date: '2024-11-18', time: '16:00', objective: 'Definir las metas a corto y largo plazo'})" },
    { "prompt": "Iniciar una reunión de coordinación para el proyecto 'Desarrollo de Nuevas Funcionalidades' el 3 de diciembre a las 9 AM", "completion": "createMeeting({project: 'Desarrollo de Nuevas Funcionalidades', date: '2024-12-03', time: '09:00', objective: 'Coordinar tareas y asignación de recursos'})" },
    { "prompt": "Reprogramar una reunión de retroalimentación para el proyecto 'Mejora de Sistemas' el 19 de noviembre a las 11 AM", "completion": "createMeeting({project: 'Mejora de Sistemas', date: '2024-11-19', time: '11:00', objective: 'Revisión de feedback y propuestas de mejora'})" },
    { "prompt": "Reunir a los equipos para discutir el proyecto 'Rediseño de Marca' el 22 de noviembre a las 2 PM", "completion": "createMeeting({project: 'Rediseño de Marca', date: '2024-11-22', time: '14:00', objective: 'Discusión sobre avances y próximos pasos'})" },
    { "prompt": "Organizar una reunión de evaluación para el proyecto 'Desarrollo de Software' el 13 de diciembre a las 10 AM", "completion": "createMeeting({project: 'Desarrollo de Software', date: '2024-12-13', time: '10:00', objective: 'Evaluación del progreso y posibles ajustes'})" },
    { "prompt": "Establecer una reunión de planificación estratégica para el proyecto 'Automatización de Marketing' el 25 de noviembre a las 3 PM", "completion": "createMeeting({project: 'Automatización de Marketing', date: '2024-11-25', time: '15:00', objective: 'Planificación de tareas y objetivos a largo plazo'})" },
    { "prompt": "Convocar una reunión ejecutiva para revisar los resultados del proyecto 'Transformación Digital' el 30 de noviembre a las 5 PM", "completion": "createMeeting({project: 'Transformación Digital', date: '2024-11-30', time: '17:00', objective: 'Revisión de resultados y decisiones estratégicas'})" },
    { "prompt": "Agendar una reunión para discutir la finalización del proyecto 'Innovación de Producto' el 1 de diciembre a las 4 PM", "completion": "createMeeting({project: 'Innovación de Producto', date: '2024-12-01', time: '16:00', objective: 'Revisión final y presentación de resultados'})" },
    { "prompt": "Organizar una reunión de revisión del proyecto 'Automatización de Marketing' el 20 de noviembre a las 11 AM", "completion": "createMeeting({project: 'Automatización de Marketing', date: '2024-11-20', time: '11:00', objective: 'Revisión de métricas y resultados'})" },
    { "prompt": "Programar una reunión ejecutiva para discutir el proyecto 'Mejora de Infraestructura' el 5 de diciembre a las 4 PM", "completion": "createMeeting({project: 'Mejora de Infraestructura', date: '2024-12-05', time: '16:00', objective: 'Análisis de avance y decisiones estratégicas'})" },
    { "prompt": "Crear una reunión de planificación para el proyecto 'Reestructuración Organizacional' el 2 de diciembre a las 10 AM", "completion": "createMeeting({project: 'Reestructuración Organizacional', date: '2024-12-02', time: '10:00', objective: 'Planificación de tareas y asignaciones'})" },

    # Asignar tareas relacionadas con reuniones importantes
    { "prompt": "Encargar a De La Cruz Gonzalez Axel Adolfo la tarea de preparar una presentación para la reunión del proyecto 'Transformación Digital' el 15 de noviembre", "completion": "assignTask({project: 'Transformación Digital', task: 'Preparar presentación para reunión', assignee: 'De La Cruz Gonzalez Axel Adolfo'})" },
    { "prompt": "Designar a Escobar Montoya Patricio la tarea de reunir datos para la reunión ejecutiva de 'Mejora de Infraestructura' del 5 de diciembre", "completion": "assignTask({project: 'Mejora de Infraestructura', task: 'Reunir datos para reunión ejecutiva', assignee: 'Escobar Montoya Patricio'})" },
    { "prompt": "Asignar a Juarez Botello Josué Adalid la tarea de redactar un informe para la reunión de revisión del proyecto 'Automatización de Marketing'", "completion": "assignTask({project: 'Automatización de Marketing', task: 'Redactar informe para reunión de revisión', assignee: 'Juarez Botello Josué Adalid'})" },
    { "prompt": "Responsabilizar a Juarez Solano Juan Martín de crear un resumen ejecutivo para la reunión de estrategia de 'Desarrollo de Software'", "completion": "assignTask({project: 'Desarrollo de Software', task: 'Crear resumen ejecutivo para reunión', assignee: 'Juarez Solano Juan Martín'})" },
    { "prompt": "Encargar a Martínez Serrano Alexis Geovanni la tarea de coordinar la logística para la reunión de planificación del proyecto 'Reestructuración Organizacional'", "completion": "assignTask({project: 'Reestructuración Organizacional', task: 'Coordinar logística para reunión', assignee: 'Martínez Serrano Alexis Geovanni'})" },
    { "prompt": "Designar a Montoya Gutierrez Pavel la tarea de reunir datos para la reunión ejecutiva de 'Mejora de Infraestructura' del 5 de diciembre", "completion": "assignTask({project: 'Mejora de Infraestructura', task: 'Reunir datos para reunión ejecutiva', assignee: 'Montoya Gutierrez Pavel'})" },
    { "prompt": "Asignar a Rodríguez Cuéllar Spencer Fabian la tarea de redactar un informe para la reunión de revisión del proyecto 'Automatización de Marketing'", "completion": "assignTask({project: 'Automatización de Marketing', task: 'Redactar informe para reunión de revisión', assignee: 'Rodríguez Cuéllar Spencer Fabian'})" },
    { "prompt": "Responsabilizar a Sireno Ojeda Cesar Abraham de crear un resumen ejecutivo para la reunión de estrategia de 'Desarrollo de Software'", "completion": "assignTask({project: 'Desarrollo de Software', task: 'Crear resumen ejecutivo para reunión', assignee: 'Sireno Ojeda Cesar Abraham'})" },
    { "prompt": "Encargar a De La Cruz Gonzalez Axel Adolfo la tarea de coordinar la logística para la reunión de planificación del proyecto 'Reestructuración Organizacional'", "completion": "assignTask({project: 'Reestructuración Organizacional', task: 'Coordinar logística para reunión', assignee: 'De La Cruz Gonzalez Axel Adolfo'})" },
    { "prompt": "Designar a Escobar Montoya Patricio la tarea de reunir datos para la reunión ejecutiva de 'Mejora de Infraestructura' del 5 de diciembre", "completion": "assignTask({project: 'Mejora de Infraestructura', task: 'Reunir datos para reunión ejecutiva', assignee: 'Escobar Montoya Patricio'})" },
    { "prompt": "Asignar a Juarez Botello Josué Adalid la tarea de redactar un informe para la reunión de revisión del proyecto 'Automatización de Marketing'", "completion": "assignTask({project: 'Automatización de Marketing', task: 'Redactar informe para reunión de revisión', assignee: 'Juarez Botello Josué Adalid'})" },
    { "prompt": "Responsabilizar a Juarez Solano Juan Martín de crear un resumen ejecutivo para la reunión de estrategia de 'Desarrollo de Software'", "completion": "assignTask({project: 'Desarrollo de Software', task: 'Crear resumen ejecutivo para reunión', assignee: 'Juarez Solano Juan Martín'})" },
    { "prompt": "Encargar a Martínez Serrano Alexis Geovanni la tarea de coordinar la logística para la reunión de planificación del proyecto 'Reestructuración Organizacional'", "completion": "assignTask({project: 'Reestructuración Organizacional', task: 'Coordinar logística para reunión', assignee: 'Martínez Serrano Alexis Geovanni'})" },
    { "prompt": "Designar a Montoya Gutierrez Pavel la tarea de reunir datos para la reunión ejecutiva de 'Mejora de Infraestructura' del 5 de diciembre", "completion": "assignTask({project: 'Mejora de Infraestructura', task: 'Reunir datos para reunión ejecutiva', assignee: 'Montoya Gutierrez Pavel'})" },
    { "prompt": "Asignar a Rodríguez Cuéllar Spencer Fabian la tarea de redactar un informe para la reunión de revisión del proyecto 'Automatización de Marketing'", "completion": "assignTask({project: 'Automatización de Marketing', task: 'Redactar informe para reunión de revisión', assignee: 'Rodríguez Cuéllar Spencer Fabian'})" },
    { "prompt": "Responsabilizar a Sireno Ojeda Cesar Abraham de crear un resumen ejecutivo para la reunión de estrategia de 'Desarrollo de Software'", "completion": "assignTask({project: 'Desarrollo de Software', task: 'Crear resumen ejecutivo para reunión', assignee: 'Sireno Ojeda Cesar Abraham'})" },
    { "prompt": "Asignar a Cesar Abraham la tarea de preparar una presentación para la reunión del proyecto 'Transformación Digital' el 15 de noviembre", "completion": "assignTask({project: 'Transformación Digital', task: 'Preparar presentación para reunión', assignee: 'Pedro Martínez'})" },
    { "prompt": "Asignar a Alexis Serrano la tarea de reunir datos para la reunión ejecutiva de 'Mejora de Infraestructura' del 5 de diciembre", "completion": "assignTask({project: 'Mejora de Infraestructura', task: 'Reunir datos para reunión ejecutiva', assignee: 'María Sánchez'})" },
    { "prompt": "Encargar a Pavel Montoya la tarea de redactar un informe para la reunión de revisión del proyecto 'Automatización de Marketing'", "completion": "assignTask({project: 'Automatización de Marketing', task: 'Redactar informe para reunión de revisión', assignee: 'Juan Pérez'})" },
    { "prompt": "Asignar a Juan Juarez Solano la tarea de crear un resumen ejecutivo para la reunión de estrategia de 'Desarrollo de Software'", "completion": "assignTask({project: 'Desarrollo de Software', task: 'Crear resumen ejecutivo para reunión', assignee: 'Laura Gómez'})" },
    { "prompt": "Asignar a Spencer Fabian Rodríguez Cuéllar la tarea de coordinar la logística para la reunión de planificación del proyecto 'Reestructuración Organizacional'", "completion": "assignTask({project: 'Reestructuración Organizacional', task: 'Coordinar logística para reunión', assignee: 'José Ramírez'})" },
    { "prompt": "Asignar a Alexi la tarea de reunir datos para la reunión ejecutiva de 'Mejora de Infraestructura' del 5 de diciembre", "completion": "assignTask({project: 'Mejora de Infraestructura', task: 'Reunir datos para reunión ejecutiva', assignee: 'María Sánchez'})" },
    { "prompt": "Encargar a Pabel la tarea de redactar un informe para la reunión de revisión del proyecto 'Automatización de Marketing'", "completion": "assignTask({project: 'Automatización de Marketing', task: 'Redactar informe para reunión de revisión', assignee: 'Juan Pérez'})" },
    { "prompt": "Asignar a Juanino  la tarea de crear un resumen ejecutivo para la reunión de estrategia de 'Desarrollo de Software'", "completion": "assignTask({project: 'Desarrollo de Software', task: 'Crear resumen ejecutivo para reunión', assignee: 'Laura Gómez'})" },
    { "prompt": "Asignar a Fabian Rodríguez Cuéllar la tarea de coordinar la logística para la reunión de planificación del proyecto 'Reestructuración Organizacional'", "completion": "assignTask({project: 'Reestructuración Organizacional', task: 'Coordinar logística para reunión', assignee: 'José Ramírez'})" },
    { "prompt": "Encargar a Axel la tarea de preparar una presentación para la reunión del proyecto 'Transformación Digital' el 15 de noviembre", "completion": "assignTask({project: 'Transformación Digital', task: 'Preparar presentación para reunión', assignee: 'Axel'})" },
    { "prompt": "Designar a Patricio la tarea de reunir datos para la reunión ejecutiva de 'Mejora de Infraestructura' del 5 de diciembre", "completion": "assignTask({project: 'Mejora de Infraestructura', task: 'Reunir datos para reunión ejecutiva', assignee: 'Patricio'})" },
    { "prompt": "Asignar a Josué la tarea de redactar un informe para la reunión de revisión del proyecto 'Automatización de Marketing'", "completion": "assignTask({project: 'Automatización de Marketing', task: 'Redactar informe para reunión de revisión', assignee: 'Josué'})" },
    { "prompt": "Responsabilizar a Juan de crear un resumen ejecutivo para la reunión de estrategia de 'Desarrollo de Software'", "completion": "assignTask({project: 'Desarrollo de Software', task: 'Crear resumen ejecutivo para reunión', assignee: 'Juan'})" },
    { "prompt": "Encargar a Alexis la tarea de coordinar la logística para la reunión de planificación del proyecto 'Reestructuración Organizacional'", "completion": "assignTask({project: 'Reestructuración Organizacional', task: 'Coordinar logística para reunión', assignee: 'Alexis'})" },
    { "prompt": "Designar a Pavel la tarea de reunir datos para la reunión ejecutiva de 'Mejora de Infraestructura' del 5 de diciembre", "completion": "assignTask({project: 'Mejora de Infraestructura', task: 'Reunir datos para reunión ejecutiva', assignee: 'Pavel'})" },
    { "prompt": "Asignar a Spencer la tarea de redactar un informe para la reunión de revisión del proyecto 'Automatización de Marketing'", "completion": "assignTask({project: 'Automatización de Marketing', task: 'Redactar informe para reunión de revisión', assignee: 'Spencer'})" },
    { "prompt": "Responsabilizar a César la tarea de crear un resumen ejecutivo para la reunión de estrategia de 'Desarrollo de Software'", "completion": "assignTask({project: 'Desarrollo de Software', task: 'Crear resumen ejecutivo para reunión', assignee: 'César'})" },
    { "prompt": "Encargar a Axel la tarea de coordinar la logística para la reunión de planificación del proyecto 'Reestructuración Organizacional'", "completion": "assignTask({project: 'Reestructuración Organizacional', task: 'Coordinar logística para reunión', assignee: 'Axel'})" },
    { "prompt": "Designar a Patricio la tarea de reunir datos para la reunión ejecutiva de 'Mejora de Infraestructura' del 5 de diciembre", "completion": "assignTask({project: 'Mejora de Infraestructura', task: 'Reunir datos para reunión ejecutiva', assignee: 'Patricio'})" },
    { "prompt": "Asignar a Josué la tarea de redactar un informe para la reunión de revisión del proyecto 'Automatización de Marketing'", "completion": "assignTask({project: 'Automatización de Marketing', task: 'Redactar informe para reunión de revisión', assignee: 'Josué'})" },
    { "prompt": "Responsabilizar a Juan la tarea de crear un resumen ejecutivo para la reunión de estrategia de 'Desarrollo de Software'", "completion": "assignTask({project: 'Desarrollo de Software', task: 'Crear resumen ejecutivo para reunión', assignee: 'Juan'})" },
    { "prompt": "Encargar a Alexis la tarea de coordinar la logística para la reunión de planificación del proyecto 'Reestructuración Organizacional'", "completion": "assignTask({project: 'Reestructuración Organizacional', task: 'Coordinar logística para reunión', assignee: 'Alexis'})" },
    { "prompt": "Designar a Pavel la tarea de reunir datos para la reunión ejecutiva de 'Mejora de Infraestructura' del 5 de diciembre", "completion": "assignTask({project: 'Mejora de Infraestructura', task: 'Reunir datos para reunión ejecutiva', assignee: 'Pavel'})" },
    { "prompt": "Asignar a Spencer la tarea de redactar un informe para la reunión de revisión del proyecto 'Automatización de Marketing'", "completion": "assignTask({project: 'Automatización de Marketing', task: 'Redactar informe para reunión de revisión', assignee: 'Spencer'})" },
    { "prompt": "Responsabilizar a César la tarea de crear un resumen ejecutivo para la reunión de estrategia de 'Desarrollo de Software'", "completion": "assignTask({project: 'Desarrollo de Software', task: 'Crear resumen ejecutivo para reunión', assignee: 'César'})" },
];

#DAR DE ALTA USUARIOS Y DAR DE BAJAS USUARIOS



# Iniciar fine-tuning con datos de entrenamiento
# fineTuneModel(trainingData)

# Verificar el estado del fine-tuning
# getFineTuneStatus("fine-tune-id-ejemplo")
