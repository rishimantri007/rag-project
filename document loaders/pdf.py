from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import TokenTextSplitter, RecursiveCharacterTextSplitter

data = PyPDFLoader("document loaders/GRU.pdf")

docs = data.load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
chunks = splitter.split_documents(docs)

print((chunks[0].page_content))