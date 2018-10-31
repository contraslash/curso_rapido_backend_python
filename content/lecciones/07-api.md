Title: API
Author: Mauricio Collazos
Date: 2018-10-12
![]()
---
class: center, middle, light, first-slide
# APIs
## Mauricio Collazos
.footnote[]
---
# HTTP
  - Recursos
  - Métodos
    - GET
    - PUT
    - POST
    - DELETE
  - Respuestas
    - 200: OK
    - 201: Created
    - 301: Moved Permanently
    - 302: Moved
    - 400: Bad Request
    - 401: Unauthorized
    - 403: Forbidden
    - 404: Not Found
    - 405: Method Not Allowed
    - 500: Internal Server Error
    - 502: Bad Gateway
    - 503: Service Unavailable
    - 504: Gateway Timeout
  - Encabezados
---
# Conceptos importantes
- Mantener todo modular
- Facil deexplorar
- Que satisfaga los requerimientos
- Facil de extender
- Mantenga tanto privado como sea posible
- Evite cambiar endpoints y especificaciones
- Que los nombres sean explicatorios
- Documente TODO
---
# No todo CRUD es RESTful
- Negociación de contenido
- HATEOAS (Hypermedia As The Engiene of Application State)
- Seguridad
- Versionamiento
---
# Representaciones
- Un recurso puede tener diferentes representaciones
- Cada representación debe tener suficiente información para modificar el objeto
---
# Librerías

- [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)
- [Django Rest Framework](https://www.django-rest-framework.org/)
