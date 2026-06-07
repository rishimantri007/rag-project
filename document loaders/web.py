# from dotenv import load_dotenv
# from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import  WebBaseLoader
# from langchain_core.prompts import ChatPromptTemplate

data = WebBaseLoader("https://www.apple.com/")

docs = data.load()

print((docs[0].page_content))