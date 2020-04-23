!pip install --user chatterbot==0.8.6
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer 
bot=ChatBot("Athira")
bot.set_trainer(ChatterBotCorpusTrainer)
bot.train("chatterbot.corpus.english")
while(1):
    message=input("you:")
    if message=="bye" or message=="Bye":
        print("{}:see you later".format(bot.name))
        break
    if message!="bye" or message!="Bye":
        reply=bot.get_response(message)
        print("{}:{}".format(bot.name,reply))
        