from fastapi import FastAPI, File, UploadFile
from fastapi.responses import StreamingResponse
from io import BytesIO

app = FastAPI()

@app.post("/segment")
async def segment_image(file: UploadFile = File(...)):
    contents = await file.read()
    return StreamingResponse(BytesIO(contents), media_type=file.content_type)

@app.post("/transform")
async def transform_image(file: UploadFile = File(...)):
    contents = await file.read()
    return StreamingResponse(BytesIO(contents), media_type=file.content_type)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)