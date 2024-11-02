from llama_index.llms.ollama import Ollama
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
import gradio as gr


embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")
llm = Ollama(model="llama3.2:1b", request_timeout=60.0)
Settings.llm = llm

documents = SimpleDirectoryReader("resources").load_data()
index = VectorStoreIndex.from_documents(documents, llm=llm, embed_model=embed_model)

query_engine = index.as_query_engine(streaming=True)

def predict(message, history):
    response = query_engine.query(message).response_gen
    buf = ''
    for text in response:
        buf += text
        yield buf

gr.ChatInterface(predict, type="messages").launch()

