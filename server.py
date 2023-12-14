import asyncio
import websockets
import main

async def handle_websocket(websocket, path):
    async for message in websocket:

        mess = message.split(" ")
        if not main.checkUserExists(mess[1], mess[0]):
            await websocket.close()
            break
        else:
            if mess[2] == "sendMessage":
                main.sendMessage(mess[4], main.getUserId(mess[1]), mess[3])
            if mess[2] == "getChats":
                await websocket.send(str(main.getChats(main.getUserId(mess[1]))).replace(" ", '%20'))
                print(str(main.getChats(main.getUserId(mess[1]))).replace(" ", '%20'))
            if mess[2] == "getChat":
                if main.checkUserInChat(main.getUserId(mess[1]), mess[3]):
                    await websocket.send(str(main.getChatMessages(mess[3])).replace(" ", '%20').replace(",", "%21"))
                    print(str(main.getChatMessages(mess[3])).replace(" ", '%20').replace(",", "%21"))
async def start_websocket_server():
    async with websockets.serve(handle_websocket, "localhost", 8765):
        await asyncio.Future()

asyncio.run(start_websocket_server())
