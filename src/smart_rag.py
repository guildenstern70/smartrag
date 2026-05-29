##
## SmartRAG Project
## (C) 2026 Alessio Saltarin
##
## License: MIT License
##


import os
from dotenv import load_dotenv, find_dotenv
import pypdf
from langchain_core.documents import Document
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma

# Load environment variables from the .env file
load_dotenv(find_dotenv())

if __name__ == "__main__":
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError(
            "GOOGLE_API_KEY is not set. Please add it to your .env file."
        )
    print("SmartRAG v.1.0")

    print("Loading PDF document...")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(script_dir, "../docs/TechCorp_Official_Employee_Handbook.pdf")
    reader = pypdf.PdfReader(pdf_path)
    document = []
    for i, page in enumerate(reader.pages):
        text = page.extract_text()
        if text:
            document.append(Document(page_content=text, metadata={"source": pdf_path, "page": i}))

    print("Chunking text...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    chunks = text_splitter.split_documents(document)

    print("Creating vector database...")
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=os.path.join(script_dir, "chroma_db")
    )

    # Configure the database to act as a document retriever
    retriever = vector_db.as_retriever(search_kwargs={"k": 2})

    # Define the hidden prompt structure for the LLM
    template = """
Use the following pieces of retrieved context to answer the question. 
If you don't know the answer, just say that you don't know. 
Use three sentences maximum and keep the answer concise.

Context: {context}

Question: {question}

Answer:
"""
    prompt = PromptTemplate.from_template(template)

    # Initialize the Gemini model
    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash", temperature=0)

    # Helper function to stitch retrieved chunks into a single text block
    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    # Connect everything together using LangChain Expression Language (LCEL)
    rag_chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
    )

    # Chat with your PDF in a continuous loop
    print("\n--- PDF Chatbot Initialized ---")
    print("Type 'exit' or 'quit' to stop.")

    while True:
        try:
            # 1. Wait for the user to type a question
            user_question = input("\nYour Question: ")
        except (KeyboardInterrupt, EOFError):
            print("\nShutting down chatbot. Goodbye!")
            break

        # 2. Allow the user to break the loop and close the program
        if user_question.lower() in ['exit', 'quit']:
            print("Shutting down chatbot. Goodbye!")
            break

        if not user_question.strip():
            continue

        print("Searching and generating answer...")
        # 3. Send the question through our RAG chain
        response = rag_chain.invoke(user_question)

        # 4. Clean up the output format
        if isinstance(response.content, list):
            clean_answer = response.content[0]['text']
        else:
            clean_answer = response.content

        # 5. Print the final answer to the console
        print(f"Answer: {clean_answer}")
