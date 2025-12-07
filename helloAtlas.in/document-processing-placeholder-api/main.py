from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/process")
async def process_file(file: UploadFile = File(...)):
    return JSONResponse({"status": "ok","testing": "newChange", "filename": file.filename})
