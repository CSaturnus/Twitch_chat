import socket
import logging
from emoji import demojize
import re
import pyautogui
import pydirectinput
import keyboard


global message

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'cptsaturn'
token = ''
channel = '#cptsaturn'

sock = socket.socket()
sock.connect((server, port))

sock.send(f"PASS {token}\n".encode('utf-8'))
sock.send(f"NICK {nickname}\n".encode('utf-8'))
sock.send(f"JOIN {channel}\n".encode('utf-8'))

resp = sock.recv(2048).decode('utf-8')

def controll(message):

    print(message)

    message = message.lower().strip()

    if "up" == message:
        pydirectinput.press("w")
        message = ""

    if "down" == message:
        pydirectinput.press("s")
        message = ""

    if "left" == message:
        pydirectinput.press("a")
        message = ""

    if "right" == message:
        pydirectinput.press("d")
        message = ""

    if "a" == message:
        pydirectinput.press("l")
        message = ""

    if "b" == message:
        pydirectinput.press("k")
        message = ""

    if "start" == message:
        pydirectinput.press("y")
        message = ""
    return

while True:
    resp = sock.recv(2048).decode('utf-8')

    message = ""
    match = re.search(':(.*)\!.*@.*\.tmi\.twitch\.tv PRIVMSG #(.*) :(.*)', resp)

    if match:
        username, channel, message = match.groups()
        controll(message)

#    if resp.startswith('PING'):
#        sock.send("PONG\n".encode('utf-8'))
    
#    elif len(resp) > 0:
#        logging.info(demojize(resp))
