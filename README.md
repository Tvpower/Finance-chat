# 🏦 Banky - Financial Document Assistant

A smart financial document assistant that uses AI to help you analyze and chat with your financial PDF documents. Upload your financial reports, statements, or any financial PDFs and get instant answers to your questions!

## 🚀 Features

- **PDF Document Upload**: Upload and process financial PDF documents
- **AI-Powered Chat**: Ask questions about your documents and get intelligent responses
- **Web Interface**: User-friendly Streamlit frontend for easy interaction
- **REST API**: FastAPI backend for document processing and chat functionality
- **Document Processing**: Advanced document processing with vector embeddings for accurate retrieval

## 🛠️ Technologies Used

### Backend
- **FastAPI**: Modern, fast web framework for building APIs
- **Uvicorn**: ASGI server for FastAPI
- **LangChain**: Framework for developing applications with large language models
- **ChromaDB**: Vector database for document embeddings and similarity search
- **Sentence Transformers**: For creating document embeddings
- **PyPDF**: PDF processing and text extraction

### Frontend
- **Streamlit**: Interactive web application framework
- **Requests**: HTTP library for API communication

## 📋 Prerequisites

- Python 3.12.3
- pip (Python package manager)
- virtualenv

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tvpower/Finance-chat
   cd Finance-chat
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
5. **Install model**
   ```bash
    cd models
   #This is an unofficial version of the model, you can directly download it from META page and convert the gguf on your own.
   #Alternatively, you can use the official version of the model from HuggingFace but the only have 8B quantized version.
    hf download legraphista/Meta-Llama-3.1-8B-Instruct-IMat-GGUF \ --include "Meta-Llama-3.1-8B-Instruct-f16.gguf" \ --local-dir 
   ```

## 🚀 How to Run

### Option 1: Run Both Services Separately (Recommended)

1. **Start the FastAPI Backend** (Terminal 1):
   ```bash
   python main.py
   ```
   The API will be available at `http://localhost:8000`

2. **Start the Streamlit Frontend** (Terminal 2):
   ```bash
   streamlit run app.py
   ```
   The web interface will open automatically in your browser at `http://localhost:8501`

### Option 2: API Documentation

Once the FastAPI backend is running, you can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📖 How to Use

1. **Access the Web Interface**: Open your browser and go to `http://localhost:8501`

2. **Upload Documents**:
   - Use the sidebar to upload a PDF file
   - Click "Process Documents" to analyze and index your document
   - Wait for the success message

3. **Chat with Your Documents**:
   - Use the main chat interface to ask questions about your uploaded documents
   - Ask questions like:
     - "What's the total revenue mentioned in this report?"
     - "What are the main financial risks identified?"
     - "Summarize the key financial metrics"

4. **Get Intelligent Responses**:
   - The AI will analyze your documents and provide contextual answers
   - All responses are based on the content of your uploaded documents

## 📁 Project Structure