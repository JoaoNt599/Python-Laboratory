from models.connection_options.connection import DBConnectionHandler


if __name__ == "__main__":

    db_handle = DBConnectionHandler()
    conn1 = db_handle.get_db_connection()
    print(conn1)

    print("+-----------------------------------------------------------------------------------------------------------+")

    db_handle.connect_to_db()
    conn2 = db_handle.get_db_connection()
    print(conn2)

    collection = conn2.get_collection("minhaCollection")
    collection.insert_one({
        "Estou": "Inserindo pelo run",
        "Numeros": [987, 654, 321]
    })
