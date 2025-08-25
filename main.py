from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os

app = FastAPI(title="Finance helper API")

UPLOAD_FOLDER = "./uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    # TODO: Triggers the document processing pipeline
    # prcess_document(file_path)

    print(f"File '{file.filename}' uploaded and saved")


    return JSONResponse(content={"file_path": file_path, "status": "processing_started"}, status_code=200)

@app.post("/chat/")
async def chat_with_doc(query: str = Form(...)):

    # TODO: Get response from the RAG pipeline
    # response = get_chat_response(query)

    print(f"Chat query: '{query}'")
    response = "placeholder for now remember to chance this :3"
    return JSONResponse(content={"response": response})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)