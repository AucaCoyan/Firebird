# Firebird Manual

Este módulo conecta con [Firebird SQL](https://firebirdsql.org/). Puedes conectarte con bases de datos .FDB y ejecutar queries.

![banner](img/Banner_Firebird.jpg)

## Como instalar este módulo

**Descarga** e **instala** el contenido en la carpeta `modules` en la ruta de rocketbot.

## Descripción de los comandos

### Conectarse a bd Firebird

Este comando conectará con la base de datos de Firebird SQL.

| Parámetros   | Descripción                                 | Ejemplo                                 |
| ------------ | ------------------------------------------- | --------------------------------------- |
| DSN Hostname | Ruta de conexión a la base de datos         | C:\/Usuario\/Desktop\/base-de-datos.FDB |
| Usuario      | Nombre del usuario                          | myuser                                  |
| Contraseña   | Contraseña de usuario                       | mypassword                              |
| Resultado    | Valor donde se asigna True en caso de éxito | result                                  |

### Ejecutar una query

Este comando ejecutará la query y guardará el resultado en la variable anotada.

| Parámetros | Descripción                               | Ejemplo               |
| ---------- | ----------------------------------------- | --------------------- |
| Query      | Query a ejecutar sobre la FDB             | SELECT \* FROM TABLE1 |
| Resultado  | Valor donde se asigna la respuesta de FDB | result                |

### Cerrar la conexión

Este comando cierra la conexión con la base de datos.

No se necesita parámetro alguno.
