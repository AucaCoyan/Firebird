# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
   sudo pip install <package> -t .

"""

GetParams = GetParams  # type: ignore
SetVar = SetVar  # type: ignore
PrintException = PrintException  # type: ignore
tmp_global_obj = tmp_global_obj  # type: ignore

import os
import sys


base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Firebird" + os.sep + "libs"

if cur_path not in sys.path:
    sys.path.append(cur_path)

# fbclient.dll path
dll_folder = os.path.join(cur_path)
dll_full_path = os.path.join(dll_folder, "fbclient.dll")

# import rocketbot implementation of fdb
import rocketbotfirebird as rbfb  # type: ignore


# Globals declared here
global mod_firebird_sessions

# Default declared here
SESSION_DEFAULT = "default"

# Initialize settings for the module here
try:
    if mod_firebird_sessions is None:  # type: ignore
        mod_firebird_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_firebird_sessions = {SESSION_DEFAULT: {}}


# capture the name of the running command
module = GetParams("module")

# get the running session, otherwise get the default session
session = GetParams("session")

if not session:
    session = SESSION_DEFAULT


if module == "connect":
    dsn = GetParams("dsn")
    user = GetParams("user")
    password = GetParams("password")
    result = GetParams("result")

    print(
        f"""
    connecting to the database with the following keys:
    session: {session}
    dsn:  {dsn}
    user:  {user}
    password: ***** (secret)
    result: {result}
    """
    )

    # Testing parameters
    debug = False
    if debug == True:
        print("debugging mode")
        user = "SYSDBA"
        password = "masterkey"
        file = r"C:/firebirdDatabase/TEST.FDB"
        # query to select all tables
        query1 = "select rdb$relation_name from rdb$relations where rdb$view_blr is null and (rdb$system_flag is null or rdb$system_flag = 0);"
        # query to select everything from the DB. It's a lot of output lines
        query2 = "SELECT * FROM RDB$RELATIONS"

        query = query1

        directorio_libreria = os.path.join(
            "C:", r"\Program Files (x86)", "Firebird", "Firebird_3_0"
        )
        ruta = os.path.join(directorio_libreria, "fbclient.dll")

        # Test por si no anda connect, cursor y query por separado
        output = rbfb.connect_and_point(
            user=user, password=password, database=file, library_path=ruta, query=query
        )
        print(output)
        exit()

    try:
        # load the connection and the cursor
        connection = rbfb.connect_fdb(
            user=user, password=password, database=dsn, library_path=dll_full_path
        )
        cursor = rbfb.cursor_fdb(connection)

        # save the connection and the cursor on the session dictionary
        mod_firebird_sessions[session] = {"connection": connection, "cursor": cursor}

        # Después de que funcione excecute, borrar esta linea y dejar result, True
        # SetVar(result, fdb_response)
        SetVar(result, True)
    except Exception as e:
        PrintException()
        raise e

if module == "execute":
    # Take the vars from frontend
    query = GetParams("query")
    result = GetParams("result")

    print(f"making the query: \n    {query} \nto the database.")
    # Recover the connection and cursor
    connection = mod_firebird_sessions[session]["connection"]
    cursor = mod_firebird_sessions[session]["cursor"]

    try:
        """
        For the writing queries, you have to write
        connection.commit()
        otherwise the client won't wrinte into the DB
        """
        if query.lower().startswith(("create", "insert", "update", "delete", "alter")):
            connection.commit()
            if result:
                SetVar(result, True)

        else:
            """
            For every other query
            """
            fdb_response = rbfb.execute_fdb(query, cursor)
            print("DB response is: ", fdb_response)
            SetVar(result, fdb_response)

    except Exception as e:
        PrintException()
        raise e


if module == "close":
    # Recover the connection and cursor
    connection = mod_firebird_sessions[session]["connection"]
    cursor = mod_firebird_sessions[session]["cursor"]

    try:
        connection.close()
    except Exception as e:
        PrintException()
        raise e
