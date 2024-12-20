from weasyprint import HTML


def generate_pdf_report(data):
    """
    Genera un PDF a partir de datos proporcionados por el cliente.

    Args:
        data (dict): Datos para personalizar el reporte.

    Returns:
        bytes: Archivo PDF en formato binario.
    """
    # Crear el contenido HTML dinámico
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; }}
            h1 {{ color: darkblue; }}
        </style>
    </head>
    <body>
        <h1>Reporte Personalizado</h1>
        <p>Hola, {data.get('name', 'Usuario')}!</p>
        <p>Este es tu reporte generado dinámicamente.</p>
        <p>Detalles: {data.get('details', 'Sin detalles')}</p>
    </body>
    </html>
    """
    # Generar el PDF
    pdf = HTML(string=html_content).write_pdf()
    return pdf
