# Tarea 1 - Consumir datos de una API utilizando herramientas de línea de comandos (curl)

## 1. Introducción a curl

### curl
curl (Client URL) es una herramienta de línea de comandos para transferir datos hacia o desde un servidor de red.

### Uso Básico
- Instalación: `curl --version`.
- Obtener Contenido de una Página Web: `curl http://example.com`.

## 2. Consumo de Datos de una API

### JSONPlaceholder
- Obtener Publicaciones: `curl https://jsonplaceholder.typicode.com/posts`.
- Obtener Encabezados: `curl -I https://jsonplaceholder.typicode.com/posts`.
- Realizar una Solicitud POST: `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`.

## Resultado Esperado
- Al ejecutar `curl --version`, se muestra la versión de curl y los protocolos admitidos.
- Al obtener publicaciones de JSONPlaceholder, se recibe una lista JSON de publicaciones.
- Al obtener solo encabezados, se muestra una salida concisa con códigos de estado y encabezados.
- Al realizar una solicitud POST, se recibe una respuesta del servidor confirmando la recepción de los datos.