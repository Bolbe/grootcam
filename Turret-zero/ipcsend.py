import sys
import ipc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("port", type=int, help="Port number of the process")
parser.add_argument("command", help="Command to be sent to the process")
parser.add_argument("--host", default="localhost", help="Remote host (default is localhost)")
args = parser.parse_args()

port = int(args.port)
command = args.command
host = args.host

print(f"Sending command [{command}] to port number [{port}] at [{host}]")
response = ipc.send(port, command, host)
print(response)
if (response==None):
    sys.exit(1)
