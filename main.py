from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()

result=chat_model.invoke ("AI에 대한 시를 써줘줘")
print(result.content)