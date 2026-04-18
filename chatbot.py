from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage , HumanMessage

model = ChatMistralAI(model="mistral-small-2501", temperature=0.9)
print("choose your AI mode")
print("press 1 for Angry mode")
print("press 2 for Funny mode")
print("press 3 for Sad mode")

choice = int (input("tekk your response :-"))

if choice == 1:
   mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif choice == 2:
   mode = "You are a very funny AI agent. You resond with humor and jokes."
elif choice == 3:
   mode = "You are a sad AI agent. You respond in a depressed and emotional tone. "


messages = [
   SystemMessage (content=mode)

]


print("--------------- Welcome type 0 to exit the application ---------- ")

while True: 
   promt = input("You : ")
   messages.append(HumanMessage(content=promt))
   if promt =="0":
      break
   response = model.invoke(messages)
   messages.append(AIMessage(content=response.content) )
   print ("Bot :",response.content)

print(messages)   