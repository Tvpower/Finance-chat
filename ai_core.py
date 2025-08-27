import fitz
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.llms.llamacpp import LlamaCpp
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import io
from langchain.docstore.document import Document

# --- Global vars ---
VECTOR_STORE = None
QA_CHAIN = None

def _ocr_image_bytess(img_bytes: bytes) -> str:
    from PIL import Image
    import pytesseract
    img = Image.open(io.BytesIO(img_bytes))
    return pytesseract.image_to_string(img)

def ocr_pdf_images(file_path: str) -> str:
    """return list[Document] with OCR text from embedded images."""
    docs = []
    with fitz.open(file_path) as pdf:
        for page_index in range(len(pdf)):
            page = pdf[page_index]
            for(xref, *_rest) in page.get_images(full=True):
                image_info = pdf.extract_image(xref)
                img_bytes = image_info.get("image")
                if not img_bytes:
                    continue
                text = _ocr_image_bytess(img_bytes).strip()
                if text:
                    docs.append(Document(
                        page_content=text,
                        metadata={"source": file_path,
                                  "page": page_index + 1,
                                  "type": "image_ocr"
                                  },
                        )
                    )
    return docs

def process_documents(file_path: str):

    global VECTOR_STORE

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    texts = text_splitter.split_documents(documents)

    ocr_docs = ocr_pdf_images(file_path)

    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    if texts:
        VECTOR_STORE = Chroma.from_documents(texts, embedding)
    else:
        VECTOR_STORE = Chroma.from_documents(collection_name = "finance docs", embedding_function = embedding)

    if ocr_docs:
        VECTOR_STORE.add_documents(ocr_docs)

    print("Docs process {Text and img OCR} and embedded >:)")

    initialize_qa_chain()


def initialize_qa_chain():
    global QA_CHAIN, VECTOR_STORE

    if VECTOR_STORE is None:
        print("Vector store not initialized. Please process a document first.")
        return

    llm = LlamaCpp(model_path="models/Llama-3.1-8B-Instruct.F16.gguf",
                   n_gpu_layers=-1, #offloads layers to gpu
                   n_batch=512,     #batch size for prompt processing
                   n_ctx=4096,      #context window size
                   verbose=True
    )

    template = """Use the following pieces of context to answer the question at the end. 
    If you don't know the answer, just say that you don't know, don't try to make up an answer.
    Keep the answer concise.
    
    Context: {context}
    
    Question: {question}
    
    Helpful Answer:
    """
    QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

    #RetrievalQA chain
    QA_CHAIN = RetrievalQA.from_chain_type(
        llm,
        retriever= VECTOR_STORE.as_retriever(),
        chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
    )
    print("QA chain initialized >:)")

def get_chat_response(query: str) -> str:

    if QA_CHAIN is None:
        return "Doc hasn't been processed yet. Please process a document first."

    result = QA_CHAIN.invoke({"query": query})
    return result["result"]
