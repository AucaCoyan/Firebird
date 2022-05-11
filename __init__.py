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

base_path = tmp_global_obj["basepath"]  # type: ignore
cur_path = base_path + "modules" + os.sep + "Firebird" + os.sep + "libs"

if cur_path not in sys.path:
    sys.path.append(cur_path)

import fdb  # type: ignore
import re
import datetime

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
module = GetParams("module")  # type: ignore

if module == "connect":
    user = GetParams("user")  # type: ignore
    password = GetParams("password")  # type: ignore
    dsnHostname = GetParams("dsnHostname")  # type: ignore
    dsnPort = GetParams("dsnPort")  # type: ignore
    dsnSID = GetParams("dsnSID")  # type: ignore
    session = GetParams("session")  # type: ignore
    result = GetParams("result")  # type: ignore
    oracle_client_path = GetParams("oracle_client_path")  # type: ignore
    dsn = ""
    data = GetParams("identifier")  # type: ignore
    option = GetParams("option")  # type: ignore

    print(f'entro al modulo {module}')

if module == "execute":
    query = GetParams("query")  # type: ignore
    session = GetParams("session")  # type: ignore
    result = GetParams("result")  # type: ignore

    if not session:
        session = SESSION_DEFAULT

    cursor = mod_firebird_sessions[session]["cursor"]
    con = mod_firebird_sessions[session]["connection"]  # type: ignore

    try:
        cursor.execute(query)
        if query.lower().startswith(("insert", "update", "delete", "alter")):
            con.commit()
            if result:
                SetVar(result, True)  # type: ignore
        # cred_oracle = {"user": user, "password": password, "dsn": dsn}
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
                    mod_firebird_sessions[session][result] = data  # type: ignore
                except:
                    mod_firebird_sessions[session][result] = data_str
                SetVar(result, data_str)  # type: ignore
    except Exception as e:
        PrintException()  # type: ignore
        raise e

if module == "close":
    session = GetParams("session")  # type: ignore

    if not session:
        session = SESSION_DEFAULT

    cursor = mod_firebird_sessions[session]["cursor"]
    con = mod_firebird_sessions[session]["connection"]

    try:
        cursor.close()
        con.close()
    except Exception as e:
        PrintException()  # type: ignore
        raise e
