from pymongo import MongoClient
import pprint
#Create instance of Mongo Client
client = MongoClient(port=27017)

#Create database
db =client.javatpoint

employee={
    "id" :"0003456",
    "name":"Xrysoula Pantsidou",
    "profession":"OIKOKURA",
}
#Creating collection
employees = db.employees

#insert data
employees.insert_one(employee)

pprint.pprint(employees.find({"name":"Xrysoula Pantsidou"}))
pprint.pprint(employees.find_one())
for e in employees.find():
    print(e)
