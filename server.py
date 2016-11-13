from websocket import create_connection
import json
import subprocess

import config

ws = create_connection("ws://achex.ca:4010")
ws.recv()

ws.send(json.dumps({
    "setID": config.robot_id,
    "passwd": "none",
}))

ws.recv()

try:
    while True:
        message = json.loads(ws.recv())
        command = message["payload"]

        try:
            output = subprocess.check_output(command + "; true", shell=True, stderr=subprocess.STDOUT).decode()
        except subprocess.CalledProcessError as e:
            pass

        message["payload"] = output
        message["to"] = message["FROM"]
        del message["FROM"]
        ws.send(json.dumps(message))
finally:
    ws.close()
