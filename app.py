# Import necessary libraries
import streamlit as st
import os
import shutil
from langchain.memory import ChatMessageHistory
import retriever
import REG_Chain
# Initialize chat history and Google Generative AI model
chat_history = ChatMessageHistory()
global chain
chain =None
if not os.path.exists('data/'):
    os.mkdir('data/')

# Function to write response
def write_response(prompt):
    # Check if PDF files have been uploaded
    if len(os.listdir('data/')) == 0:
        st.sidebar.warning('Please upload your files to chat')
        return
    # Add user message to session state and chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar='🧑‍💼'):
        st.write(prompt)
    chat_history.add_user_message(prompt)
    
    # Get response from retriever and chain
    with st.chat_message("assistant", avatar='✨'):
        with st.spinner('Thinking...'):
            res = chain.invoke({'chat_history':chat_history.messages , 'question': prompt})
            st.write(res)
            st.session_state.messages.append({'role': 'assistant', 'content': res})
            chat_history.add_ai_message(res)
#clear Chat History
def clear_history():
    st.session_state.messages=[{'role': 'assistant', 'content': 'Chat with Your Provided Documents'}]
    chat_history.clear()

# Streamlit sidebar title and file upload
st.sidebar.title('Chatbot utilizing your documents with Gemini AI ♊')
st.sidebar.markdown("If you'd like to 🗣️ chat with PDF docs, please 📤 upload them below 👇🏻")
pdf_files = st.sidebar.file_uploader("Upload a PDF File", type=['pdf'], help='Please Upload Your Pdf File', accept_multiple_files=True)
st.sidebar.button('Clear Chat history',on_click=clear_history)
# Save uploaded PDF files in data folder
if pdf_files:
    shutil.rmtree('data/')
    os.mkdir('data/')
    for file in pdf_files:
        with open(os.path.join('data', file.name), 'wb') as temp:
            temp.write(file.read())
    retriever = retriever.save_doc_as_vector_retriever()
    st.sidebar.success('File upload Success')
    chain=REG_Chain.get_REG_chain()

# Create data folder if no PDF files are uploaded
if len(pdf_files) == 0:
    shutil.rmtree('data/')
    os.mkdir('data/')

# Initialize messages in session state
if 'messages' not in st.session_state.keys():
    st.session_state.messages = [{'role': 'assistant', 'content': 'Chat with Your Provided Documents'}]

# Display messages in chat
for message in st.session_state.messages:
    if message['role'] == 'assistant':
        with st.chat_message(message["role"], avatar='✨'):
            st.write(message["content"])
            chat_history.add_ai_message(message["content"])
    else:
        with st.chat_message(message["role"], avatar='🧑‍💼'):
            st.write(message["content"])
            chat_history.add_user_message(message["content"])

# Chat input and response
if prompt := st.chat_input():
    write_response(prompt)
