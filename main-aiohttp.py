import aiohttp
from aiohttp import web


async def index_handler(request: web.Request) -> web.FileResponse:
    return web.FileResponse("index.html")


async def websocket_handler(request: web.Request) -> web.WebSocketResponse:
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            await ws.send_str(f"echo '{msg.data}'")

    return ws


app = web.Application()
app.add_routes([web.get("/", index_handler)])
app.add_routes([web.get("/ws", websocket_handler)])

web.run_app(app, port=22614)
