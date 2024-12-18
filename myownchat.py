import os
import constants
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain import hub
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# Set up environment variables
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = constants.LANGCHAINKEY
os.environ["OPENAI_API_KEY"] = constants.APIKEY
os.environ['USER_AGENT'] = 'myagent'

# Initialize LLM and embeddings
llm = ChatOpenAI(model="gpt-4")
embedding = OpenAIEmbeddings()

# Load and split documents
raw_documents = TextLoader('./data/calender.txt').load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
documents = text_splitter.split_documents(raw_documents)

# Create vector store from documents
vectorstore = Chroma.from_documents(documents=documents, embedding=embedding)

# Load prompt from hub
prompt = hub.pull("rlm/rag-prompt")

# Format function for documents
def format_docs(documents):
    return "\n\n".join(doc.page_content for doc in documents)

# Setup retriever
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 6})

# Create the RAG chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def chat_with_documents():
    print("Welcome to the Document ChatBot! Type 'quit' to exit.")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
            
        try:
            # Get response from the RAG chain
            response = rag_chain.invoke(user_input)
            print("\nBot:", response)
            
        except Exception as e:
            print(f"\nError: An error occurred - {str(e)}")
            print("Please try again with a different question.")

if __name__ == "__main__":
    chat_with_documents()
