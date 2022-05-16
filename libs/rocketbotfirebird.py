import os
import fdb


def connect_and_point(user, password, database, library_path, query):
    """original func.
    Now its separated in connect_fdb and cursor_fdb
    """
    connection = fdb.connect(
        dsn=database, user=user, password=password, fb_library_name=library_path
    )
    cursor = connection.cursor()

    cursor.execute(query)
    return cursor.fetchall()


def connect_fdb(user, password, database, library_path):

    connection = fdb.connect(
        dsn=database, user=user, password=password, fb_library_name=library_path
    )
    return connection


def cursor_fdb(connection):
    cursor = connection.cursor()
    return cursor


def execute_fdb(query, cursor):
    # cursor.execute("SELECT * FROM RDB$RELATIONS")
    cursor.execute(query)
    fdb_response = cursor.fetchall()
    return fdb_response


def close_conn_fdb(connection):
    connection.close()


if __name__ == "__main__":
    user = "SYSDBA"
    password = "masterkey"
    file = r"C:/firebirdDatabase/TEST.FDB"
    directorio_libreria = os.path.join(
        "C:", "\Program Files (x86)", "Firebird", "Firebird_3_0"
    )
    ruta = os.path.join(directorio_libreria, "fbclient.dll")
    print("la ruta de dll es ", ruta)

    # connect_fdb(user=user, password=password, database=file, library_path=ruta)
    connection = connect_fdb(
        user=user, password=password, database=file, library_path=ruta
    )
    cursor = cursor_fdb(connection)
    response_fdb = execute_fdb("SELECT * FROM RDB$RELATIONS", cursor)
    print(response_fdb)

    # print(connect_and_point(user=user, password=password, database=file, library_path=ruta))
