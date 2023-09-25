from pymongo import MongoClient

#########################################
# DETAILS
#########################################
url = "<your-cluster-link>"
client = MongoClient(url)

# Send a ping to connection
try:
    client.admin.command('ping')
    print("Database is online.")
except Exception as e:
    print(e)

# Creating a database.
db = client.SIH_23