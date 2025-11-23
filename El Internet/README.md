# RESTful API - Documentación

## Descripción General

**Nombre de la API:** RESTful API (api.restful-api.dev)

**Descripción:** API REST real, lista para gestionar tus solicitudes HTTP las 24 horas del día, los 7 días de la semana, de forma gratuita. Se puede utilizar para tus proyectos de demostración, pruebas, aprendizaje o incluso para formar a otras personas. Esta API REST es compatible con los principales métodos HTTP, como GET, POST, PUT, DELETE y PATCH.

**URL Base:** `https://api.restful-api.dev`

---

## Endpoints y Solicitudes

### 1. POST - Crear un Nuevo Objeto

**Método HTTP:** `POST`

**Endpoint:** `/objects`

**URL Completa:** `https://api.restful-api.dev/objects`

**Parámetros/Cuerpo de la Solicitud:**
```json
{
   "name": "One Plus 12",
   "data": {
      "year": 2024,
      "price": 800,
      "CPU model": "Snapdrago 8 Gen 3 Mobile",
      "Hard disk size": "512 GB"
   }
}
```

**Descripción:** Crea un nuevo objeto con la información proporcionada. La API genera automáticamente un ID único y una marca de tiempo de creación. El ID único del nuevo objeto creado se guarda como una variable de entorno.

**Ejemplo de Respuesta:**
```json
{
   "id": "ff8081819782e69e019aae9f0c3c5597",
   "name": "One Plus 12",
   "createdAt": "2025-11-23T02:50:50.301+00:00",
   "data": {
      "year": 2024,
      "price": 800,
      "CPU model": "Snapdrago 8 Gen 3 Mobile",
      "Hard disk size": "512 GB"
   }
}
```

**Código de Estado:** `200 OK`

---

### 2. GET - Obtener un Objeto Específico

**Método HTTP:** `GET`

**Endpoint:** `/objects/{id}`

**URL Completa:** `https://api.restful-api.dev/objects/{{ObjectID}}`

**Parámetros:** 
- `id` (path parameter): ID único del objeto que se quiere obtener

**Descripción:** Recupera la información de un objeto específico utilizando su ID único. En este caso el mismo objeto creado en el POST, ya que se pasa la variable que contiene el ID del objeto creado en el POST.

**Ejemplo de Respuesta:**
```json
{
   "id": "ff8081819782e69e019aae9f0c3c5597",
   "name": "One Plus 12",
   "data": {
      "year": 2024,
      "price": 800,
      "CPU model": "Snapdrago 8 Gen 3 Mobile",
      "Hard disk size": "512 GB"
   }
}
```

**Código de Estado:** `200 OK`

---

### 3. PUT - Actualizar/Reemplazar un Objeto

**Método HTTP:** `PUT`

**Endpoint:** `/objects/{id}`

**URL Completa:** `https://api.restful-api.dev/objects/{{ObjectID}}`

**Parámetros/Cuerpo de la Solicitud:**
```json
{
   "name": "One Plus 13",
   "data": {
      "year": 2025,
      "price": 1100,
      "CPU model": "Snapdrago 8 Gen 5 Mobile",
      "Hard disk size": "512 GB"
   }
}
```

**Descripción:** Reemplaza completamente la información de un objeto existente. Mantiene el ID original pero actualiza todos los demás campos y agrega una marca de tiempo de actualización. En este caso el mismo objeto creado en el POST, ya que se pasa la variable que contiene el ID del objeto creado en el POST.

**Ejemplo de Respuesta:**
```json
{
   "id": "ff8081819782e69e019aae9f0c3c5597",
   "name": "One Plus 13",
   "updatedAt": "2025-11-23T02:52:23.321+00:00",
   "data": {
      "year": 2025,
      "price": 1100,
      "CPU model": "Snapdrago 8 Gen 5 Mobile",
      "Hard disk size": "512 GB"
   }
}
```

**Código de Estado:** `200 OK`

---

### 4. GET - Obtener Lista de Objetos

**Método HTTP:** `GET`

**Endpoint:** `/objects`

**URL Completa:** `https://api.restful-api.dev/objects?id=3&id=5&id=10&id={{ObjectID}}`

**Parámetros:** 
- `id` (query parameters): Múltiples IDs de objetos que se desean obtener

**Descripción:** Recupera una lista de objetos específicos utilizando sus IDs como parámetros de consulta. Permite obtener múltiples objetos en una sola solicitud. En este caso incluye el mismo objeto creado en el POST, ya que se pasa la variable que contiene el ID del objeto creado en el POST.

**Ejemplo de Respuesta:**
```json
[
   {
      "id": "3",
      "name": "Apple iPhone 12 Pro Max",
      "data": {
         "color": "Cloudy White",
         "capacity GB": 512
      }
   },
   {
      "id": "5",
      "name": "Samsung Galaxy Z Fold2",
      "data": {
         "price": 689.99,
         "color": "Brown"
      }
   },
   {
      "id": "10",
      "name": "Apple iPad Mini 5th Gen",
      "data": {
         "Capacity": "64 GB",
         "Screen size": 7.9
      }
   },
   {
      "id": "ff8081819782e69e019aae9f0c3c5597",
      "name": "One Plus 13",
      "data": {
         "year": 2025,
         "price": 1100,
         "CPU model": "Snapdrago 8 Gen 5 Mobile",
         "Hard disk size": "512 GB"
      }
   }
]
```

**Código de Estado:** `200 OK`

---

### 5. DELETE - Eliminar un Objeto

**Método HTTP:** `DELETE`

**Endpoint:** `/objects/{id}`

**URL Completa:** `https://api.restful-api.dev/objects/{{ObjectID}}`

**Parámetros:** 
- `id` (path parameter): ID único del objeto que se quiere eliminar

**Descripción:** Elimina permanentemente un objeto del sistema utilizando su ID único. En este caso el mismo objeto creado en el POST, ya que se pasa la variable que contiene el ID del objeto creado en el POST.

**Ejemplo de Respuesta:** {"message":"Object with id = ff8081819782e69e019aae9f0c3c5597 has been deleted."}

**Código de Estado:** `200 OK`

---

## Headers Utilizados

En todas las solicitudes se utilizó el siguiente header:
```
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
```

## Variables de Entorno

- **ObjectID**: Variable que almacena el ID del objeto creado mediante el POST, utilizada en las demás solicitudes para referenciar el objeto específico.

---

## Aprendizajes del Proceso

Durante el trabajo con esta API REST se aprendió:

1. **Operaciones CRUD Completas**: La API implementa todas las operaciones básicas (Create, Read, Update, Delete) que son fundamentales en cualquier sistema REST.

2. **Variables de Entorno en Postman**: El uso de variables como `{{ObjectID}}` permite crear flujos de trabajo automatizados donde el resultado de una operación alimenta las siguientes.

3. **Códigos de Estado HTTP**: Comprensión práctica de los códigos de respuesta HTTP y su significado en el contexto de operaciones REST.

4. **Estructura JSON**: Práctica en el manejo de estructuras JSON tanto para envío de datos como para interpretación de respuestas.