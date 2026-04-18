from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("openai/gpt-oss-120b", model_provider="groq",temperature = 0,max_tokens = 20 ) 
response = model.invoke("write a poem on AI ")
print(response.content)

""" you can use model class also ...for that go to langchain docs , "temperature is for creativity ,,the more temperature is the more creativity is , this max tokens is for limiting the tokens that we are taking only 20 toekens that means answer wil be in 20 tokens only (for limiting the tokens )"""