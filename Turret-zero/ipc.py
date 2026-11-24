from multiprocessing.connection import Listener
from multiprocessing.connection import Client

def listen(port_number, handler):
    
    listener = Listener(('localhost', port_number))
    print(f"IPC listener started: {port_number}")

    while True:
        try:
            conn = listener.accept()
            command = conn.recv()
            if (command=="ping"):
                response = True
            else:    
                response = handler(command)
            conn.send(response)
            conn.close()
        except Exception as e:
            print(f"ERROR: Listener {port_number}:\n{e}")
            if (conn!=None):
                conn.close()
 
def send(port_number, command, host='localhost'):

    try:
        conn = Client((host, port_number))
        conn.send(command)
        response = conn.recv()
        conn.close()
        return response
    except Exception as e:
        print(f"IPC: cannot connect to {host}:{port_number}")
        return None
