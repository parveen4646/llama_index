from llama_index import VectorStoreIndex, SimpleDirectoryReader,StorageContext,ServiceContext
from llama_index.schema import Document
import pdfplumber
from dotenv import load_dotenv
import os
import  openai
load_dotenv()
openai.api_key=os.getenv('OPENAI_API_KEY')
from llama_index import download_loader
PDFPlumberReader = download_loader("PDFPlumberReader")
loader = PDFPlumberReader()

def parse_pdf(file_path):
    documents = loader.load_data(file=file_path)
    return documents        

def get_indexing(documents,input_text):    
    service_context=ServiceContext.from_defaults(chunk_size=500)
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_chat_engine(streaming=False,chat_mode='condense_plus_context')
    response = query_engine.chat(input_text)     
    return response.response
    

    
