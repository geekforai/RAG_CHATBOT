# Chatbot with Gemini AI

Chatbot with Gemini AI is a Python-based application that allows users to interact with PDF documents using the Gemini AI model.

## Features

- Upload PDF documents for chatbot interaction.
- Utilizes Gemini AI for natural language processing.
- Simple and intuitive interface.
## Overview of the chatbot architecture
![Architecture](https://python.langchain.com/assets/images/conversational_retrieval_chain-5c7a96abe29e582bc575a0a0d63f86b0.png)

Certainly! Let's delve into the details of the architecture depicted in the image:

1. **History-Aware Retriever**:
   - This component is responsible for retrieving relevant information based on the user's query while considering the context from previous interactions (chat history).
   - Here's how it works:
     - **Input Query**: The system receives a user query (e.g., "What is the capital of France?").
     - **Contextualization**: The query is contextualized using information from the chat history. This step ensures that the system understands the query in the context of the ongoing conversation.
     - **Language Learning Model (LLM)**: The contextualized query is passed to an LLM, which has been trained to understand natural language. The LLM processes the query and identifies relevant keywords or concepts.
     - **Retrieval**: Using the information from the LLM, the system retrieves relevant documents or data. These documents could be articles, web pages, or any other sources containing relevant information related to the query.

2. **Question Answer Join**:
   - Once the relevant documents are retrieved, the system aims to generate a concise and accurate answer to the user's question.
   - Here's how this part works:
     - **Documents**: The retrieved documents (e.g., articles, FAQs, etc.) serve as the basis for answering questions.
     - **Answer Prompt**: The system uses another prompt (similar to the user query) to generate an answer. This prompt is designed to extract relevant information from the documents.
     - **LLM for Answering**: An LLM processes the answer prompt and generates a coherent response. It considers the context from the chat history and the retrieved documents.
     - **Answer Generation**: The LLM produces an answer based on the information it has learned. This answer is then presented to the user.

3. **Context Matters**:
   - The key innovation here is the consideration of context. By analyzing the chat history, the system can provide more accurate and contextually relevant answers.
   - For example, if the user previously asked about French cuisine, the system would understand that the query "What is the capital of France?" likely refers to Paris.

In summary, this architecture combines natural language understanding, document retrieval, and context-awareness to enhance the quality of responses in a question-answering system. Feel free to ask if you'd like further clarification or have additional questions! 😊
## Installation

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
    streamlit runn app.py
    ```

2. Follow the prompts to upload PDF documents and interact with the chatbot.

## Contributing

Contributions are welcome! If you have any ideas or suggestions for improvement, feel free to open an issue or submit a pull request.
