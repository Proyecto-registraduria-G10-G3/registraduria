import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient(
    "mongodb+srv://equipo3:P4$$w0rd@cluster0.wijocek.mongodb.net/registraduria?retryWrites=true&w=majority",
    tlsCAFile=ca
)

db = client.test
print(db)

data_base = client['registraduria']
print(data_base.list_collection_names())

candidate = data_base.get_collection('candidate')




