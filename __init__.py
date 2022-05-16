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

GetParams = GetParams #type: ignore
SetVar = SetVar #type: ignore
PrintException = PrintException #type: ignore
tmp_global_obj = tmp_global_obj #type: ignore

import os, sys


base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Firebird" + os.sep + "libs"

if cur_path not in sys.path:
    sys.path.append(cur_path)

# fbclient.dll path
dll_folder = os.path.join(cur_path)
dll_full_path = os.path.join(dll_folder, 'fbclient.dll')


import re
import datetime

# import rocketbot implementation of fdb
import rocketbotfirebird as rbfb #type: ignore


# Globals declared here
global mod_firebird_sessions

# Default declared here
SESSION_DEFAULT = "default"

# Initialize settings for the module here
try:
    if mod_firebird_sessions is None: #type: ignore
        mod_firebird_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_firebird_sessions = {SESSION_DEFAULT: {}}


# capture the name of the running command
module = GetParams("module")

if module == "connect":
    session = GetParams("session")
    dsn = GetParams("dsn")
    user = GetParams("user")
    password = GetParams("password")
    result = GetParams("result")

    print(f"""
    session: {session}
    dsn:  {dsn}
    user:  {user}
    password {password}
    result: {result}
    """)
    # capture the running session (if any)
    if not session: #type: ignore
        session = SESSION_DEFAULT

    debug = True

    if debug == True:
        # Testing parameters
        # user = "SYSDBA"
        # password = "masterkey"
        # file = r"C:/firebirdDatabase/TEST.FDB"
        directorio_libreria = os.path.join("C:", "\\Program Files (x86)", "Firebird", "Firebird_3_0")
        ruta = os.path.join(directorio_libreria, "fbclient.dll")

        # Test por si no anda connect, cursor y query por separado
        salida = rbfb.connect_and_point(user=user, password=password, database=dsn, library_path=ruta)
        print(salida)

        # exit the command
        exit()

    try:
        # load the connection and the cursor 
        connection = rbfb.connect_fdb(user=user, password=password, database=dsn, library_path=dll_full_path)
        cursor = rbfb.cursor_fdb(connection)

        # save the connection and the cursor on the session dictionary 
        mod_firebird_sessions[session] = {
            "connection": connection,
            "cursor": cursor
        }

        # Después de que funcione excecute, borrar esta linea y dejar result, True
        # SetVar(result, fdb_response)
        SetVar(result, True)
    except Exception as e:
        PrintException()
        raise e
    
    """
    finally:
        rbfb.close_conn_fdb(connection)
        pass
    """

if module == "execute":
    """
    Para las queries, si son de escribir en la base de datos tenés que mandarle
    connection.commit()
    sino no te las escribe
    """
    # Take the vars from frontend
    session = GetParams("session")
    print('la sesion es:', session)
    query = GetParams("query")
    result = GetParams("result")


    if not session: #type: ignore
        session = SESSION_DEFAULT

    # Recover the connection and cursor
    connection = mod_firebird_sessions[session]['connection']
    cursor = mod_firebird_sessions[session]['cursor']

    try:
        if query.lower().startswith(("create", "insert", "update", "delete", "alter")):
            connection.commit()
            if result:
                SetVar(result, True)

        else:
            # Esto no sé para qué sirve
            """
            data = [r for r in cursor]
            regex = r"datetime.datetime\(\d\d\d\d,\s?\d\d,\s?\d\d?,\s?\d\d?,\s?\d\d?,?\s?\d?\d?\)"
            regex2 = r"datetime.datetime\(\d\d\d\d,\s?\d,\s?\d\d?,\s?\d\d?,\s?\d\d?,?\s?\d?\d?\)"
            data_str = str(data)
            matches = re.finditer(regex, data_str, re.MULTILINE)
            matches2 = re.finditer(regex2, data_str, re.MULTILINE)
            for match in matches:
                data_str = data_str.replace(
                    match.group(),
                    '"{}"'.format(eval(match.group()).strftime("%d/%m/%Y")),
                )
            for match in matches2:
                data_str = data_str.replace(
                    match.group(),
                    '"{}"'.format(eval(match.group()).strftime("%d/%m/%Y")),
                )
            try:
                data = eval(data_str)
                mod_firebird_sessions[session][result] = data
            except:
                mod_firebird_sessions[session][result] = data_str
            SetVar(result, data_str)
            """

            fdb_response = rbfb.execute_fdb(query, cursor)
            print('la respuesta es: ', fdb_response)
            SetVar(result, fdb_response)

    except Exception as e:
        PrintException()
        raise e


if module == "close":
    session = GetParams("session")

    if not session: #type: ignore
        session = SESSION_DEFAULT

    # Recover the connection and cursor
    connection = mod_firebird_sessions[session]['connection']
    cursor = mod_firebird_sessions[session]['cursor']

    try:
        # cursor.close() # esto creo que no hace falta
        connection.close()
    except Exception as e:
        PrintException()
        raise e
