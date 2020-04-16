import socket
import threading
from queue import Queue

print_lock = threading.Lock()
target = 'pythonprogramming.net'

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port',port, 'is open!!')
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(1000):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

print_lock
for worker in range(1,6500000):
    q.put(worker)

q.join()