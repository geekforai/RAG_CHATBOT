# Chatbot with Gemini AI

Chatbot with Gemini AI is a Python-based application that allows users to interact with PDF documents using the Gemini AI model.

## Features

- Upload PDF documents for chatbot interaction.
- Utilizes Gemini AI for natural language processing.
- Simple and intuitive interface.
## Overview of the chatbot architecture


## Architecture
![Architecture](https://python.langchain.com/assets/images/conversational_retrieval_chain-5c7a96abe29e582bc575a0a0d63f86b0.png)


### History-Aware Retriever:

The History-Aware Retriever component is responsible for retrieving relevant information based on the user's query while considering the context from previous interactions (chat history). Here's how it works:

1. **Input Query:** The system receives a user query (e.g., "What is the capital of France?").
2. **Contextualization:** The query is contextualized using information from the chat history to understand it within the ongoing conversation.
3. **Language Learning Model (LLM):** The contextualized query is passed to an LLM, which identifies relevant keywords or concepts.
4. **Retrieval:** Using the information from the LLM, the system retrieves relevant documents or data, such as  PDF articles or web pages.

### Question Answer Join:

Once the relevant documents are retrieved, the system aims to generate a concise and accurate answer to the user's question. Here's how this part works:

1. **Documents:** The retrieved documents serve as the basis for answering questions.
2. **Answer Prompt:** The system uses another prompt similar to the user query to generate an answer, extracting relevant information from the documents.
3. **LLM for Answering:** An LLM processes the answer prompt and generates a coherent response considering the context from the chat history and the retrieved documents.
4. **Answer Generation:** The LLM produces an answer based on the learned information, which is then presented to the user.

### Context Matters:

The key innovation lies in considering context. By analyzing the chat history, the system can provide more accurate and contextually relevant answers. For example, if the user previously asked about French cuisine, the system would understand that the query "What is the capital of France?" likely refers to Paris. In summary, this architecture combines natural language understanding, document retrieval, and context-awareness to enhance the quality of responses in a question-answering system.

## Explanation of RAG, vectordb, Embedding, and LLM Frameworks


### LLM (Language Learning Model):

In summary, these frameworks play crucial roles in modern NLP systems. RAG combines retrieval and generation, vectordb efficiently handles embeddings, embeddings capture semantic relationships, and LLMs understand and generate natural language. Their synergy enables powerful applications across various domains.

If you'd like further details or have more questions, feel free to ask! 😊

##  Instructions for setting up the environment and running the chatbot.

1. Clone the repository:

    ```bash
    git clone https://github.com/geekforai/RAG_CHATBOT.git
    ```

2. Navigate to the project directory:

    ```bash
    cd RAG_CHATBOT
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:

    ```bash
    streamlit run app.py
    ```

2. Follow the prompts to upload PDF documents and interact with the chatbot.

## Contributing

Contributions are welcome! If you have any ideas or suggestions for improvement, feel free to open an issue or submit a pull request.
