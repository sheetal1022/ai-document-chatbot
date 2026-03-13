from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import shutil

from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

API_KEY = "AIzaSyDy4X5qOxPGxcZyhi5ic8rrB-ghdO1lBHQ"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    path = f"docs/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    loader = PyPDFLoader(path)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(
    	model_name="all-MiniLM-L6-v2"
    )

    Chroma.from_documents(
        chunks,
        embeddings,
        persist_directory="./db"
    )

    return {"message": "PDF processed successfully"}

@app.get("/ask")
def ask_question(question: str):

    embeddings = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="./db",
        embedding_function=embeddings
    )

    docs = db.similarity_search(question)

    context = " ".join([doc.page_content for doc in docs])

    return {
        "answer": context[:500]
    }