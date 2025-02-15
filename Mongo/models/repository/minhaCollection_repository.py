from bson.objectid import ObjectId
from typing import Dict, List


class MinhaCollectionRepository:
    def __init__(self, db_connection) -> None:
        self.__connection_name = "minhaCollection"
        self.__db_connection = db_connection


    # Insert
    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__connection_name)
        collection.insert_one(document)
        return document

    
    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__connection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents


    # Busca
    def select_many(self, filter) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__connection_name)
        data = collection.find(
            filter,  # Filtro
            {"endereco": 0, "_id": 0}  # Opções de retorno
        )

        response = [] 
        for i in data: response.append(i)

        return response
    

    def select_one(self, filter) -> Dict:
        collection = self.__db_connection.get_collection(self.__connection_name)
        response = collection.find_one(filter, {"_id": 0})
        return response
         
    
    def select_it_property_exists(self) -> None:
        collection = self.__db_connection.get_collection(self.__connection_name)
        data = collection.find({"cpf": {"$exists": True}})
        for i in data: print(i)

    
    def select_many_order(self):
        collection = self.__db_connection.get_collection(self.__connection_name)
        data = collection.find(
            {"nome": "Jaum"}, # Filtro
            {"endereco": 0, "_id": 0}  # Opções de retorno
        ).sort([("pedidos.pizza", -1)])

        response = [] 
        for i in data: response.append(i)

        return response
    

    def select_or(self) -> None:
        collection = self.__db_connection.get_collection(self.__connection_name)
        data = collection.find(
            { "$or": [ { "nome": "Jaum" }, {"ola": { "$exists": True } }] }
            )
        
        for i in data: 
            print(i)
            print()
    

    def select_by_object_id(self) -> None:
        collection = self.__db_connection.get_collection(self.__connection_name)
        data = collection.find({"_id": ObjectId("67b079d93b2c2191ab2f2bd8") })
        for i in data: print(i)


    # Edit
    def edit_registry(self, name) -> None:
        collection = self.__db_connection.get_collection(self.__connection_name)
        data = collection.update_one(
            { "_id": ObjectId("67b09e0ab4e33ce485423d49") }, # Filtro
            { "$set": {"nome": name} }
        )
        if data.modified_count > 0:
            print("Doc atualizado")
        else:
            print("Campo já atualizado.")
        print(data.modified_count)

    
    def edit_many_registries(self, filtro, propriedades) -> None:
        collection = self.__db_connection.get_collection(self.__connection_name)
        data = collection.update_many(
            filtro, #Filtro
            { "$set": {"profissao": propriedades} }
        )
        if data.modified_count > 0:
            print("Doc atualizado")
        else:
            print("Campo já atualizado.")
        print(data.modified_count)


    # Delete
    def delete_registry(self) -> None:
        collection = self.__db_connection.get_collection(self.__connection_name)
        data = collection.delete_many({ "apelido": "Jaum" })
        print(data.deleted_count)