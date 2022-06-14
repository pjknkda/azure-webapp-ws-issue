from fastapi import FastAPI, WebSocket
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def get():
    return FileResponse("index.html")


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    async for data in websocket.iter_text():
        await websocket.send_text(f"echo '{data}'")
