from pymongo import MongoClient
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

client = MongoClient(
    "insert your API KEY for MongoDB Cluster")
chat_db = client.get_database("SentimentChatDB")
data = chat_db.messages

chat_history = data.find()
text_file = open("text_analysis.txt", "w") #Create a empty file "text_analysis" to store incoming data from db.

for item in chat_history:
    print(str(item["created_at"]) + " - " + item["sender"] + ": " + item["text"])

# item["sender"] + "-" + file=text_file
