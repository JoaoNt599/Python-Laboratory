from bson.objectid import ObjectId
from typing import Dict, List


class MinhaCollectionRepository:
    def __init__(self, db_connection) -> None:
        self.__connection_name = "minhaCollection"
        self.__db_connection = db_connection


    def insert_document(self, document: Dict) -> Dict:
        collection = self.__db_connection.get_collection(self.__connection_name)
        collection.insert_one(document)
        return document

    
    def insert_list_of_documents(self, list_of_documents: List[Dict]) -> List[Dict]:
        collection = self.__db_connection.get_collection(self.__connection_name)
        collection.insert_many(list_of_documents)
        return list_of_documents


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