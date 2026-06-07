from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import TokenTextSplitter

data = PyPDFLoader("document loaders/GRU.pdf")

docs = data.load()
splitter = TokenTextSplitter(chunk_size=100, chunk_overlap=0)
chunks = splitter.split_documents(docs)

print(len(chunks))