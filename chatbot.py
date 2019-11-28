from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import datetime
from chatterbot.logic import LogicAdapter

# chatbot = ChatBot(
#     'Alexa',
#     storage_adapter='chatterbot.storage.SQLStorageAdapter',
#     database_uri='sqlite:///database.sqlite3'
# )

chatbot = ChatBot(
    'Alexa',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.BestMatch',
        #'chatterbot.logic.TimeLogicAdapter'
        #{
        #    'import_path': 'chatterbot.logic.BestMatch'
        #},
        #{
        #    'import_path': 'chatterbot.logic.LowConfidenceAdapter',
        #    'threshold': 0.70,
         #   'default_response': 'I am sorry, but I do not understand.'
        #}
],
    database_uri='sqlite:///database.sqlite3'
    # read_only=True
)

#chatbot = ChatBot("Alexa")
#print(chatbot)

# conversation = [
#     "Hello",
#     "Hi There",
#     "How are you doing",
#     "I am doing great.",
#     "That is good to hear",
#     "Thank You",
#     "You are welcome."
# ]
# trainer = ListTrainer(chatbot)
# trainer.train(conversation)

trainer = ChatterBotCorpusTrainer(chatbot)
# trainer.train(
#     "chatterbot.corpus.english"
# )
trainer.train(
    #"chatterbot.corpus.custom.myown",
    "chatterbot.corpus.english.ai",
    "chatterbot.corpus.english.science"
)
# trainer.train(
#     "./data/greetings_corpus/custom.corpus.json",
#     "./data/my_corpus/"
# )

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning Sir!")

    elif hour>=12 and hour<18:
        print("Good Afternoon Sir!")   

    else:
        print("Good Evening Sir!")
    print("I am Atithi, How may i help you ?")
	
wishMe()
#, I am atithi, i help tourists in every possible way , How may i help you sir?
while True:
	message = input('you:')
	reply = chatbot.get_response(message)
	print('Atithi:',reply)
	if message.strip() == 'Bye' or message.strip() == 'bye':
		print('Atithi: Bye')
		break
 #   try:
	# response = chatbot.get_response(input())
	# print(response)		

#while True:
  #      bot_input = chatbot.get_response(input())
   #     print("bot :", bot_input)
#
 #   except(KeyboardInterrupt, EOFError, SystemExit):
  #      break
        


