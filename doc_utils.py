# Import necessary libraries
import pinecone 
import langchain
from langchain.document_loaders.pdf import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores.pinecone import Pinecone
from langchain.vectorstores.faiss import FAISS

import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Configure Google Generative AI with API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to load PDF documents from a directory
def load_pdf(directory):
    # Create a PyPDFDirectoryLoader object to load PDF documents from the directory
    loader = PyPDFDirectoryLoader(directory)
    # Load the documents
    doc = loader.load()
    return doc

# Function to split a document into smaller chunks
def doc_to_chunk(doc):
    # Create a RecursiveCharacterTextSplitter object to split the document into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    # Split the document into chunks
    return splitter.split_documents(doc)

# Function to get Google Generative AI embeddings
def get_embeddings():
    # Create a GoogleGenerativeAIEmbeddings object with the specified model
    embedding = GoogleGenerativeAIEmbeddings(model='models/embedding-001')
    return embedding
