from models.connection_options.connection import DBConnectionHandler
from models.repository.minhaCollection_repository import MinhaCollectionRepository


if __name__ == "__main__":

    db_handle = DBConnectionHandler()
    db_handle.connect_to_db()
    db_connection = db_handle.get_db_connection()

    minha_collection_repository = MinhaCollectionRepository(db_connection)

    # order = {
    #     "nome": "Jaum",
    #     "endereco": "Rua La",
    #     "pedidos": {
    #         "hotdog": 2,
    #         "pizza": 10,
    #         "esfiha": 5
    #     },
    #     "cpf": '132.dgt.337'
    # }

    # minha_collection_repository.insert_document(order)

    # list_of_documents = [
    #     {"RBR": "Super Max"},
    #     {"Aston Martin": "Strollada"},
    #     {"Ferrari": "Halmiton"},
    #     {"Gabriel": "Barboleto"},
    #     {"Mclaren": "By Lando By Lando"}
    # ]

    # minha_collection_repository.insert_list_of_documents(list_of_documents)

    response = minha_collection_repository.select_many({"nome": "Jaum"})
    print(response)
    print()

    response2 = minha_collection_repository.select_one({"nome": "Jaum"})
    print(response2)
    print()

    minha_collection_repository.select_it_property_exists()
    print()

    minha_collection_repository.select_many_order()
    print()

    minha_collection_repository.select_or()
    print()

    minha_collection_repository.select_by_object_id()
    print()



    
