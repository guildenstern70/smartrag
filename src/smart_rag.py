##
## SmartRAG Project
## (C) 2026 Alessio Saltarin
##
## License: MIT License
##


import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough

# Load environment variables from the .env file
load_dotenv()

if __name__ == "__main__":
    print("SmartRAG v.1.0")
    print("Loading PDF document...")
    loader = PyPDFLoader("../docs/TechCorp_Official_Employee_Handbook.pdf")
    document = loader.load()

    print(document[0].page_content)
