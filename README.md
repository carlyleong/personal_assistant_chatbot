# RAG-Powered Document Chatbot

A conversational AI chatbot that uses Retrieval-Augmented Generation (RAG) to answer questions about your documents using LangChain and OpenAI's GPT-4.

## 🌟 Features

- Document-based question answering using RAG architecture
- Powered by OpenAI's GPT-4 and LangChain
- Vector storage using Chroma DB
- Automatic document chunking and embedding
- Simple command-line interface
- Error handling and graceful exit

## 📋 Prerequisites

- Python 3.8+
- OpenAI API key
- LangChain API key

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rag-document-chatbot.git
cd rag-document-chatbot
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `constants.py` file with your API keys:
```python
APIKEY = "your-openai-api-key"
LANGCHAINKEY = "your-langchain-api-key"
```

## 📁 Project Structure

```
rag-document-chatbot/
│
├── src/
│   ├── __init__.py
│   ├── chatbot.py          # Main chatbot implementation
│   └── constants.py        # API keys and configuration
│
├── data/
│   └── calendar.txt        # Your document file
│
├── requirements.txt        # Project dependencies
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## 🚀 Usage

1. Place your document in the `data` folder.

2. Run the chatbot:
```bash
python src/chatbot.py
```

3. Start asking questions about your document. Type 'quit' to exit.

## 📝 Example Interaction

```
Welcome to the Document ChatBot! Type 'quit' to exit.

You: What events are scheduled for next week?

Bot: Let me check the calendar for you...
[Bot provides response based on document content]

You: quit
Goodbye!
```

## ⚙️ Configuration

You can modify the following parameters in `chatbot.py`:

- `chunk_size`: Size of document chunks (default: 1000)
- `chunk_overlap`: Overlap between chunks (default: 0)
- `search_kwargs`: Number of chunks to retrieve (default: k=6)

## 📄 Required Files

1. `requirements.txt`:
```
langchain-openai
langchain-community
langchain-text-splitters
langchain-core
chromadb
openai
```

2. `.gitignore`:
```
# Python
__pycache__/
*.py[cod]
*$py.class
venv/

# Environment variables
constants.py
.env

# IDE
.vscode/
.idea/

# Database
*.db
*.sqlite

# Logs
*.log
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.
