import time
import websockets
import asyncio
import os
import threading

user_input = ""

async def send_message(message: str, chat : int):
    message = message.replace(" ", "%20")
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send(f"test 33leon3@gmx.de sendMessage {chat} {message}")

async def getchat(chat):
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send(f"test 33leon3@gmx.de getChat {chat}")
        response = await websocket.recv()
        print(response.replace("%20", " ").replace("%21", "\n").replace("%22",",")[1:-1])

async def getchats():
    async with websockets.connect('ws://localhost:8765') as websocket:
        await websocket.send("test 33leon3@gmx.de getChats")
        response = await websocket.recv()
        print(response.replace("%20", " "))

def user_input_thread(IN):
    global user_input
    while True:
        user_input = input("leerer Input aktualisiert Seite, type %q to quit chat : ")
        os.system('cls' if os.name == 'nt' else 'clear')  # clear console
        asyncio.run(getchat(IN))

def main():
    global user_input
    while True:
        asyncio.run(getchats())
        IN = input("an welchen chat soll die Nachricht gesendet werden, type %q to quit : ")
        if IN == "%q":
            break
        IN = int(IN)
        asyncio.run(getchat(IN))
        threading.Thread(target=user_input_thread, args=(IN,)).start()
        while True:
            if user_input == "":
                asyncio.run(getchat(IN))
                time.sleep(2)  
            elif user_input=="%q":
                break
            else:
                asyncio.run(send_message(user_input, IN))
                asyncio.run(getchat(IN))
                user_input = ""

if __name__ == '__main__':
    main()
