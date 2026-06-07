from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
# from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

#.env file me jo bhi variables hai unko load karne ke liye use hota hai
load_dotenv()

# data = TextLoader("document loaders/notes.txt")
data = PyPDFLoader("document loaders/GRU.pdf")
model = ChatMistralAI(model="mistral-small-2603")
docs = data.load()
template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a text summarizer."),
        ("human", "{data}"),
    ]
)

prompt = template.format_messages(data=docs)

result = model.invoke(prompt)
print(result.content)