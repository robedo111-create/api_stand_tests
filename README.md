# Proyecto de Automatización de Pruebas API

Este proyecto contiene pruebas automatizadas para la API del servicio de TripleTen, desarrolladas como parte del Sprint 8 del curso de QA Engineer.

## Estructura del Proyecto
- `configuration.py`: Contiene la URL del servicio y las rutas de los endpoints.
- `sender_stand_request.py`: Define las funciones para realizar las peticiones HTTP (GET, POST).
- `data.py`: Contiene los datos de prueba (cuerpos de solicitud y cabeceras).
- `create_user_test.py` y `create_kit_name_kit_test.py`: Contienen los scripts de pruebas con sus respectivas aserciones.

## Requisitos para ejecutar
- Python 3.x
- Librerías: `pytest`, `requests`