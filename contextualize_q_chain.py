from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder 
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage
from dotenv import load_dotenv 
load_dotenv()

#This function initializes a pipeline using Google's Generative 
# AI to rephrase user questions, making them understandable without the context of chat history.

def get_contextualize_chain():
    llm=GoogleGenerativeAI(model='gemini-pro')

    contextualize_q_system_prompt = """Given a chat history and the latest user question \
    which might reference context in the chat history, formulate a standalone question \
    which can be understood without the chat history. Do NOT answer the question, \
    just reformulate it if needed and otherwise return it as is."""

    contextualize_q_prompt= ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_q_system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}"),
        ]
    )


    contextualize_q_chain = contextualize_q_prompt | llm | StrOutputParser()
    return contextualize_q_chain


