#from flask import request, Flask,send_file
import asyncio
import websockets
from requests import post
from random import randrange

#app = Flask(__name__)

prefix = "f1"
id = "893888755449069598"
token = "YOUR_TOKEN_DISCORD_HERE"

def send_msg(id,msg):
    print(f"[send msg] {msg}")
    post(f"https://discordapp.com/api/v9/channels/{id}/messages",json={"content":msg,"nonce":randrange(1111111111111111, 99999999999999999),"tts":False},headers={"authorization": token,"user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9003 Chrome/91.0.4472.164 Electron/13.4.0 Safari/537.36"})

def check_null(data):
    if data == "" or data == None:
        return True
    return False

async def hello(websocket, path):
    print("[ws] someone connected")
    await websocket.send("Hi")
    while True :
        msg = await websocket.recv()
        print(f"[ws] msg : {msg}")
        if check_null(msg):
            pass
        elif "เปิดเพลง" in msg:
            msg = msg.replace("เปิดเพลง", "")
            if not check_null(msg):
                send_msg(id, f"{prefix}p {msg}" )
        elif "ข้ามเพลง" in msg:
            if not check_null(msg):
                send_msg(id, f"{prefix}s")
        elif "คิว" in msg:
            send_msg(id, f"{prefix}q")
        elif "ทดสอบ" in msg:
            send_msg(id, "test")
        

start_server = websockets.serve(hello, '127.0.0.1', 8765)

loop = asyncio.get_event_loop()
loop.run_until_complete(start_server)
loop.run_forever()
'''
@app.route('/', methods=['POST'])
def api_send_msg():
    print("[api] got msg")
    data = request.get_json(force=True)
    msg = data["msg"]
    print(msg)
    if check_null(msg):
        return "null"
    if "เปิดเพลง" in msg:
        msg = msg.replace("เปิดเพลง", "")
        if not check_null(msg):
            send_msg("893888755449069598", f"{prefix}p{msg}" )
    if "ข้ามเพลง" in msg:
        if not check_null(msg):
            send_msg("893888755449069598", f"{prefix}s")
    if "ทดสอบ" in msg:
        send_msg("893888755449069598", "test")
    return "ok"

@app.route('/', methods=['GET'])
def api_home():
    return send_file("index.html")
app.run(host='127.0.0.1', port=8480, threaded=False)
'''