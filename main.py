from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
import os
from ai_core import process_documents, get_chat_response

app = FastAPI(title="Finance helper API")

UPLOAD_FOLDER = "./uploads"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    try:
        process_documents(file_path)
        return JSONResponse(content={"file_path": file_path, "status": "processing_finished"}, status_code=200)

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

    return JSONResponse(content={"file_path": file_path, "status": "processing_started"}, status_code=200)

@app.post("/chat/")
async def chat_with_doc(query: str = Form(...)):

    response = get_chat_response(query)
    return JSONResponse(content={"response": response})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)