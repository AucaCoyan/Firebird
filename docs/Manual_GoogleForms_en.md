# Manual GoogleForms

This module connects to the [Google Forms API](https://developers.google.com/forms/api). You can connect to, create, read and retrieve responses from Google Forms

![banner](img/Banner_GoogleForms.jpg)

## How to install this module

**Download** and **install** the content in `modules` folder in Rocketbot path

## How to use this module

To use this module you need to configure the credentials to connect with the Google Forms API. To this, you need to follow the steps below:

- Create a new project in Google Cloud Console (Skip if you already have a project created)

  - At the top-left, click **Menu** > **IAM & Admin** > **Create a Project**.
  - In the **Project Name** field, enter a descriptive name for your project.
  - Complete the other steps with your information

- Enable API:

  - Go to [Google Cloud Console](https://console.cloud.google.com/)
  - At the top-left, click **Menu** > **APIs & Services** > **Library**
  - In the browser field, enter **Google Forms API**
  - Click in the result **Google Forms API**
  - Click **Enable**

- Register OAuth Consent:

  - Go to [Google Cloud Console](https://console.cloud.google.com/)
  - At the top-left, click **Menu** > **APIs & Services** > **OAuth consent Screen**
  - Pick **External** and click **Create**
  - Write an **App name** and an **User support email**
  - Down below complete the **Email Addresses** field on the section **Developer contact information**
  - Click **Save and continue**
  - In the second step **Scopes** click on **Save and continue**
  - In the third step **Test Users** click on **Add user** and fill an email adress
  - Afterwards, click con **Save and continue**
  - Finally, click on **Back to dashboard**

- Create Credentials:

  - Go to [Google Cloud Console](https://console.cloud.google.com/)
  - At the top-left, click **Menu** > **APIs & Services** > **Credentials**
  - Click **Create credentials**
  - Click **OAuth client ID**
  - In the **Application type** field, select **Desktop Application**
  - In the **Name** field, enter a descriptive name for the credentials
  - Appears a window with the credentials data. Click **Download JSON**
  - Use this file as credentials in the module

## Description of commands

### Connect with Google Forms

Connect with google forms will load the credentials files as indicated by the first field. Afterwards, in a success case the bot will write True in the designated variable

| Parameters                | Description                                                                                                | Example                             |
| ------------------------- | ---------------------------------------------------------------------------------------------------------- | ----------------------------------- |
| Credentials file path     | JSON file with the credentials to access the Google Forms API. See the documentation for more information. | C:\/User\/Desktop\/credentials.json |
| Assign result to variable | Name of the variable where the result of the execution of the command will be assigned.                    | result                              |

### Create Form

This command will create a form with a title specified on the field, in a success case the bot will write True in the designated variable

| Parameters                | Description                                                                             | Example       |
| ------------------------- | --------------------------------------------------------------------------------------- | ------------- |
| Form Title                | Title of the form which will be created                                                 | My Form Title |
| Assign result to variable | Name of the variable where the result of the execution of the command will be assigned. | result        |

### Read Form

This command will read the metadata of the form. You have to specify the FormID, which is found inbetween `/d/` and `/edit/` part of the link.

For example, for this link `https://docs.google.com/forms/d/168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w/edit` the `id` is `168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w`

Afterwards, the return will be stored in the variable called

| Parameters                | Description                                                                             | Example                                      |
| ------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------- |
| FormID                    | The form id that will be looked up for to fetch the metadata                            | 168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w |
| Assign result to variable | Name of the variable where the result of the execution of the command will be assigned. | result                                       |

### Retrieve the responses of a form

This command collects all the responses sent to a form by a certain FormID. You have to specify the FormID, which is found inbetween `/d/` and `/edit/` part of the link

For example, for this link `https://docs.google.com/forms/d/168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w/edit` the `id` is `168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w`

Afterwards, the return will be stored in the variable called

| Parameters                | Description                                                                             | Example                                      |
| ------------------------- | --------------------------------------------------------------------------------------- | -------------------------------------------- |
| FormID                    | The form id that will be lookup for to fetch the metadata                               | 168WM6YPG8B8PR6M5ipixcsT82b2d09lV4zrrt9b1m1w |
| Assign result to variable | Name of the variable where the result of the execution of the command will be assigned. | result                                       |
