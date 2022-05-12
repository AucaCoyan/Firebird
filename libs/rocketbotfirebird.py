import os
import fdb


def connect_fdb(user, password, file, library_path):

    connection = fdb.connect(
        database=file, user=user, password=password, fb_library_name=library_path
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM RDB$RELATIONS")
    return cursor.fetchall()



if __name__ == "__main__":
    user = "SYSDBA"
    password = "masterkey"
    file = r"C:/firebirdDatabase/TEST.FDB"
    directorio_libreria = os.path.join(
        "C:", "\Program Files (x86)", "Firebird", "Firebird_3_0"
    )
    ruta = os.path.join(directorio_libreria, "fbclient.dll")
    print("la ruta de dll es ", ruta)

    connect_fdb(user=user, password=password, file=file, library_path=ruta)

