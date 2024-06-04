# # Tarea 0 - Fundamentos de HTTP/HTTPS

## 1. Diferencias entre HTTP y HTTPS

### Definición de HTTP
        HTTP (HyperText Transfer Protocol) es un protocolo de comunicación utilizado para transferir información en la web.

### Definición de HTTPS
        HTTPS (HyperText Transfer Protocol Secure) es una versión segura de HTTP, utiliza SSL/TLS para encriptar los datos transferidos.

## Comparación
        - **Encriptación:** ---- Evitar que roben, modifiquen, alteren datos.
        - HTTP: No encripta datos.
        - HTTPS: Utiliza SSL/TLS para encriptar datos.

        - **Puerto:** -----Interaz donde se envian y reciben diferentes tipos de datos.
        - HTTP: Usa el puerto 80 por defecto.
        - HTTPS: Usa el puerto 443 por defecto.

        - **Seguridad:**
        - HTTP: Vulnerable a ataques.
        - HTTPS: Proporciona confidencialidad e integridad de datos.

### Conclusión
        El uso de HTTPS es fundamental para proteger la integridad y la privacidad de la información que se transfiere en la web.
---

-------------------------------------


## 2. Estructura de HTTP

### Request HTTP

#### Request Line
`GET/HTTP/1.1`
#### Request Headers
- Host: example.com
- User-Agent: Mozilla/5.0

### Response HTTP
#### Status Line
`HTTP/1.1 200 OK`
#### Response Headers
- Content-Type: text/html
- Content-Length: 1256

### Capturas de Pantalla
![Solicitud HTTP](ruta/a/la/captura.png)

---

## 3. Métodos y Códigos de Estado HTTP

### Métodos HTTP
- **GET:** Recupera, obtiene datos...
- **POST:** Crea datos...
- **PUT:** Actualiza datos completamente...
- **PATCH:** Actualiza datos parcialmente...
- **DELETE:** Elimina datos...

### Códigos de Estado HTTP
- **200 OK:** Solicitud exitosa.
- **201 CREADO:** Recurso creado exitosamente.
- **400 Mala Solicitud:** Solicitud incorrecta o mal formada.
- **404 Not Found:** Recurso no encontrado.
- **500 Internal Server Error:** Error en el servidor.
- **301 Moved Permanently:** Recurso movido.