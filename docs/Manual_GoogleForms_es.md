# GoogleForms Manual

Este módulo conecta con [Google Forms API](https://developers.google.com/forms/api). Puedes conectarte con, crear, leer y recolectar respuestas de Google Forms

![banner](img/Banner_GoogleForms.jpg)

## Como instalar este módulo

**Descarga** e **instala** el contenido en la carpeta `modules` en la ruta de rocketbot.

## Cómo usar este módulo

Para utilizar este módulo necesitas habilitar la API de Google Admin para tu cuenta. Para ello, debes seguir los siguientes pasos ( [referencia](https://developers.google.com/admin-sdk/directory/v1/quickstart/python) ):

- Crear un projecto en Google Cloud Console (Saltar si ya tienes un proyecto creado)

  - En el menú de la izquierda, dar click en **Menu** > **IAM & Admin** > **Create a project**
  - En el campo **Project Name**, agregar un nombre para el proyecto
  - Completar los siguientes campos según corresponda

- Habilitar la API:

  - Ir a [Google Cloud Console](https://console.cloud.google.com/)
  - En el menú arriba a la derecha, dar click en **Menu** > **APIs & Services** > **Library**
  - En el buscador, buscar **Google Forms API**
  - Dar click en el resultado **Google Forms API**
  - Click en el botón **Habilitar**

- Registrar consentimiento de OAuth:

  - Ir a [Google Cloud Console](https://console.cloud.google.com/)
  - En el menú arriba a la derecha, dar click en **Menu** > **API & Servicios** > **Pantalla de consentimiento de OAuth**
  - Elegir **Externos** y click en **Crear**
  - Completar el campo **Nombre de la aplicacion** y **Correo electrónico de asistencia del usuario**
  - Más abajo, antes del final, completar el field **Direcciones de correo electrónico** del apartado **Información de contacto del desarrollador**
  - Hacer click en **Guardar y continuar**
  - En el paso 2 **Permisos** hacer click en **Guardar y continuar**
  - En el paso 3 **Usuarios de prueba** hacer click en **Add users** y escribir la direccion de correo
  - Click en **Guardar y continuar**
  - Finalizar clickeando **Volver al panel**

- Crear credenciales de Google:

  - Ir a [Google Cloud Console](https://console.cloud.google.com/)
  - En el menú arriba a la derecha, dar click en **Menu** > **APIs & Services** > **Credentials**
  - Click en el botón **Create credentials**
  - Click en **OAuth client ID**
  - En el campo **Application type**, seleccionar **Desktop Application**
  - Escribir un nombre en el campo **Name**
  - Aparecerá una ventana con los datos de la credencial. Dar click en **Download JSON**
  - Utilizar este archivo como credenciales en el módulo

## Descripción de los comandos

### Conectar con Formularios de Google

Conectar con formularios cargará el archivo según la ruta del archivo de credenciales y se conectará con Google Forms. En caso de éxito grabará True en la variable designada para grabar el resultado

| Parámetros                       | Descripción                                                                                                                  | Ejemplo                                 |
| -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- |
| Ruta del archivo de credenciales | Archivo JSON con las credenciales de acceso a la API de Google Forms. Revisar la documentación para obtener más información. | C:\/Usuario\/Desktop\/credenciales.json |
| Asignar resultado a variable     | Nombre de la variable donde se asignará el resultado de la execución del comando.                                            | result                                  |

### Crear Formulario

Este comando creará un nuevo formulario cuyo título es el del primer campo. En caso de éxito grabara True en la variable indicada

| Parámetros                   | Descripción                                                                      | Ejemplo                 |
| ---------------------------- | -------------------------------------------------------------------------------- | ----------------------- |
| Título del Form              | Título del formulario que va a ser creado                                        | Mi Título de Formulario |
| Asignar resultado a variable | Nombre de la variable donde se asignará el resultado de la execución del comando | result                  |

### Leer Formulario

Este commando buscara la metadata del form. Para eso se necesita especificar el FormID, el cual se encuentra en el link, despues de `/d/` and `/edit/`.

Por ejemplo, en `https://docs.google.com/forms/d/168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w/edit` el `id` es `168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w`

Luego, se guardará la informacion en la variable indicada

| Parámetros                   | Descripción                                                                      | Ejemplo                                      |
| ---------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------- |
| FormID                       | El form id que va a ser buscado para recolectar la metadata                      | 168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w |
| Asignar resultado a variable | Nombre de la variable donde se asignará el resultado de la execución del comando | result                                       |

### Recolectar respuestas de un formulario

Este comando junta todas las respuestas enviadas al formulario, segun su correspondiente FormID. El FormID se encuentra en el link, despues de `/d/` and `/edit/`.

Por ejemplo, en `https://docs.google.com/forms/d/168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w/edit` el `id` es `168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w`

Luego, se guardará la informacion en la variable indicada

| Parámetros                   | Descripción                                                                      | Ejemplo                                      |
| ---------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------- |
| FormID                       | El form id que va a ser buscado para recolectar la metadata                      | 168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w |
| Asignar resultado a variable | Nombre de la variable donde se asignará el resultado de la execución del comando | result                                       |
