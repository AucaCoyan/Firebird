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


import os, sys

base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "Firebird" + os.sep + "libs"

if cur_path not in sys.path:
    sys.path.append(cur_path)

import fdb   
import re
import datetime


# Globals declared here
global mod_firebird_sessions

# Default declared here
SESSION_DEFAULT = "default"

# Initialize settings for the module here
try:
    if mod_firebird_sessions is None:
        mod_firebird_sessions = {SESSION_DEFAULT: {}}
except NameError:
    mod_firebird_sessions = {SESSION_DEFAULT: {}}





# capture the name of the running command
module = GetParams("module")

GetParams = GetParams #type: ignore

session = GetParams("session")
if not session:
    session = SESSION_DEFAULT

if module == "connect":
    """
    user = GetParams("user")
    password = GetParams("password")
    dsnHostname = GetParams("dsnHostname")
    dsnPort = GetParams("dsnPort")
    dsnSID = GetParams("dsnSID")
    
    result = GetParams("result")
    oracle_client_path = GetParams("oracle_client_path")
    dsn = ""
    data = GetParams("identifier")
    option = GetParams("option")
    """

    api_path = os.path.join(cur_path, 'fbclient.dll')

    # print('el archivo path es un file?', os.path.isfile(api_path))

    # fdb.load_api(api_path)

    # print('importo bien')









    try:




        user = "SYSDBA"
        password = "masterkey"
        file = r"C:/firebirdDatabase/TEST.FDB"
        directorio_libreria = os.path.join('C:', '\Program Files (x86)', 'Firebird', 'Firebird_3_0')
        ruta = os.path.join(directorio_libreria, 'fbclient.dll')

        from rocketbotfirebird import connect_fdb #type: ignore
        print(connect_fdb(user=user, password=password, file=file,library_path=ruta) )
        exit()

        print(ruta)
        print('el archivo existe?', os.path.isfile(ruta))

        try:
            print(dir(fdb.load_api(ruta)))

        except Exception as e:
            PrintException()
            raise e

        connection = fdb.connect(
            database=file, user=user, password=password,
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM RDB$RELATIONS")

        exit()


        connection = fdb.connect(database=dsnHostname, user=user, password=password)
        print('esto no debe aparecer')
        mod_firebird_sessions[session] = connection

    except Exception as e:
        PrintException()  # 
        raise e

if module == "execute":
    query = GetParams("query")  # 
    result = GetParams("result")  # 
    connection = mod_firebird_sessions[session]
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        print(cursor.fetchall())

        if query.lower().startswith(("insert", "update", "delete", "alter")):
            con.commit()
            if result:
                SetVar(result, True)  # 

        else:
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

            if result:
                try:
                    data = eval(data_str)
                    mod_firebird_sessions[session][result] = data  # 
                except:
                    mod_firebird_sessions[session][result] = data_str
                SetVar(result, data_str)  # 
    except Exception as e:
        PrintException()  # 
        raise e

if module == "close":
    session = GetParams("session")  # 
    cursor = mod_firebird_sessions[session]["cursor"]
    con = mod_firebird_sessions[session]["connection"]

    try:
        cursor.close()
        con.close()
    except Exception as e:
        PrintException()  # 
        raise e
