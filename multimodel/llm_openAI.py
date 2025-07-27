# uisng openAI 
'''
from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


llm = OpenAI(model="gpt-3.5-turbo-instruct", max_tokens=10)

result = llm.invoke("what do you know about me?")

print(result)
'''

### using ChatModel -? chatmodel fined tunned and structured for conversational use.
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
llm_chat = ChatOpenAI(model="gpt-4", temperature=0.7, max_completion_tokens=15)

result = llm_chat.invoke("what is chatmodel?")

print(result.content)

