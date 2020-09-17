from flask import Flask,render_template,request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Train the data
app = Flask(__name__) 
bot = ChatBot("Chatterbot",storage_adapter="chatterbot.storage.SQLStorageAdapter")
trainer = ChatterBotCorpusTrainer(bot)

trainer.train("chatterbot.corpus.english")
trainer.train("data/data.yml")


@app.route("/")
def index():
     return render_template("index.html") 

@app.route("/get")
def get_bot_response():
     userText = request.args.get("getData") 
     return str(bot.get_response(userText))
@app.route("/index2")
def inde():

     return render_template("index2.html")




if __name__ == "__main__":
     app.run(debug = True)