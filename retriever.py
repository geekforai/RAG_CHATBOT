# Import necessary libraries
import pinecone 
from langchain.vectorstores.pinecone import Pinecone
import  doc_utils
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import  AIMessage,HumanMessage
from langchain.memory import ChatMessageHistory
from langchain.vectorstores.faiss import FAISS
import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Function to save documents as vectors in the retriever
def save_doc_as_vector_retriever():
    # Directory containing the documents
    directory = 'data/'
    # Load PDF documents from the directory
    doc = doc_utils.load_pdf(directory=directory)
    # Split the document into chunks
    doc_chunk = doc_utils.doc_to_chunk(doc=doc)
    # Create a FAISS retriever from the document chunks and embeddings
    retriever = FAISS.from_documents(documents=doc_chunk, embedding=doc_utils.get_embeddings())
    retriever.save_local('faissIndex')
    # Convert the retriever to a retriever object
    return retriever.as_retriever( search_type = "similarity",search_kwargs = {"k":6})


    




        
        
    
    



