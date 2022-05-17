# Manual GoogleForms

This module connects with [Firebird SQL](https://firebirdsql.org/). You can connect to .FDB databases and execute queries.

![banner](img/Banner_Firebird.jpg)

## How to install this module

**Download** and **install** the content in `modules` folder in Rocketbot path

## Description of commands

### Connect Firebird db

This command will connect Rocketbot with the Firebird SQL database.

| Parameters   | Description                              | Example                              |
| ------------ | ---------------------------------------- | ------------------------------------ |
| DSN Hostname | Connection route                         | C:\/User\/Desktop\/base-de-datos.FDB |
| User         | Name of the user                         | myuser                               |
| Password     | Password of the user                     | mypassword                           |
| Result       | True will be asignated in case of sucess | result                               |

### Execute a query

This command will execute the query on the connected database.

| Parameters | Description                              | Example               |
| ---------- | ---------------------------------------- | --------------------- |
| Query      | Query that will be runned                | SELECT \* FROM TABLE1 |
| Result     | Variable where the return will be stored | result                |

### Close the connection

This command will close the connection of the database.

No parameters are needed.
