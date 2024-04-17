from langchain.prompts import ChatPromptTemplate,MessagesPlaceholder
from dotenv import load_dotenv
from contextualize_q_chain import get_contextualize_chain
from langchain_google_genai import GoogleGenerativeAI
from retriever import save_doc_as_vector_retriever
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

contextualize_q_chain=get_contextualize_chain()
llm=GoogleGenerativeAI(model='gemini-pro')
qa_system_prompt = """You are an assistant for question-answering tasks. \
Use the following pieces of retrieved context to answer the question. \
If you don't know the answer, just say that you don't know. \
Use three sentences maximum and keep the answer concise.\
{context}"""

load_dotenv()
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)
def contextualized_question(input: dict):
    if input.get("chat_history"):
        return contextualize_q_chain
    else:
        return input["question"]
def get_REG_chain():
    retriever=save_doc_as_vector_retriever()
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{question}"),
        ]
    )
    rag_chain = (
        RunnablePassthrough.assign(
            context = contextualized_question | retriever | format_docs
        )
        | qa_prompt 
        | llm
        | StrOutputParser()
    )
    return rag_chain
    