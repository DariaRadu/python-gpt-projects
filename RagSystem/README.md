# Small RAG System from scratch

This project is a small recreation of a RAG system tutorial that helped with understanding the basic concepts of Retrieval Augmented Generation. The tutorial can be found here: [Link](https://buildrag.com/)


## **Features**
- **Document Embedding**: Uses a custom `embedder` function to compute semantic embeddings for a corpus of text.
- **Semantic Search**: Finds the top \( k \) most relevant chunks of text from the corpus using cosine similarity.
- **AI-Powered Answer Generation**: Leverages OpenAI's GPT-4 model to generate answers based on the retrieved relevant contexts.
- **Customizable Corpus and Queries**: Easily adaptable for different datasets and query types.

## **Requirements**
- Python 3.8+
- `transformers` (for embedding models)
- `numpy`
- `openai`
- `dotenv`


## Installation

1. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure environment variables**:
    Create a `.env` file in the project root directory and add your OpenAI API key:
    ```env
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

Run `python app.py` and you are good to go!

