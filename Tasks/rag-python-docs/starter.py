from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.embeddings import resolve_embed_model
from llama_index.llms.ollama import Ollama

documents = SimpleDirectoryReader("data").load_data()

# bge embedding model
Settings.embed_model = resolve_embed_model("local:BAAI/bge-small-en-v1.5")

# ollama
Settings.llm = Ollama(model="mistral", request_timeout=30.0)

index = VectorStoreIndex.from_documents(
    documents,
)
print(index)

query_engine = index.as_query_engine()
response = query_engine.query("how to find all txt files in the current directory?")
print(response)
