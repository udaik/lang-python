import csv
from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017/')

db = client['accounts']

collection = db['transactions']

transactions = db.transactions

with open('trx.csv', 'r') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        transaction = { 'date' : row[1],
                        'description' : row[2],
                        'cheque' : row[3],
                        'debit' :  row[4],
                        'credit' : row[5],
                        'balance' : row[6],
                        'category': row[7],
                        'remarks': row[8],
                        'account' : "HDFC Bank"}
        transactionId = transactions.insert_one(transaction).inserted_id
        print(transactionId)

client.close()
