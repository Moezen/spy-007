from websocket import create_connection
import json
import sys

import config

ws = create_connection("ws://achex.ca:4010")
ws.recv()

ws.send(json.dumps({
    "setID": config.commander_id,
    "passwd":"none",
}))

ws.recv()

try:
    while True:
        sys.stdout.write("> ")
        sys.stdout.flush()
        command = sys.stdin.readline().strip()

        ws.send(json.dumps({
            "to": config.robot_id,
            "payload": command,
        }))

        message = json.loads(ws.recv())
        output = message["payload"]
        sys.stdout.write(output)
finally:
    ws.close()
