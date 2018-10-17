Title: Autenticación
Author: Mauricio Collazos
Date: 2018-10-17
![]()
---
Pendientes

- [Almacenamiento S3](https://blog.contraslash.com/almacenar-archivos-en-s3-desde-django/)
- [Migrar a MySQL](https://blog.contraslash.com/migrar-de-sqlite3-a-mysql-django/)

---
class: center, middle, light
# Autenticación
## Mauricio Collazos

---
# Objetivo
Verificar la identidad de un usuario
  
---
# Tipos
- Basic
- Bearer
- Digest
- HOBA
- Mutual

---
# JWT
- [Especificación](https://tools.ietf.org/html/rfc7519)
- Header.Payload.Signature
Header
```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```
Payload
```json
{
  "sub": "1234567890",
  "name": "John Doe",
  "admin": true
}
```
Signature

---
# Librerías
- [JWTCrypto](https://github.com/latchset/jwcrypto/)
- [Python-Jose](https://github.com/mpdavis/python-jose/)
- [PyJWT](https://github.com/jpadilla/pyjwt/)
- [AuthLib](https://github.com/lepture/authlib)