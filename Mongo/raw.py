from pymongo import MongoClient

# Connection 
connection_string = "mongodb://localhost:27017/?authSource=admin"
client = MongoClient(connection_string)
db_connection = client["meuBanco"]
print(db_connection)

print()

collection = db_connection.get_collection("minhaCollection")
print(collection)


# Filter
# search_filter = { "ola": "mundo" }
search_filter = { "estou": "aqui" }
print()

response = collection.find(search_filter)
print(response)

for registry in response: print(registry)


# Insert
collection.insert_one({
    "Estou": "Inserindo",
    "Numeros": [123, 456, 789]
})