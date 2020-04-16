import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'pythonprogramming.net'


def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for x in range(1,25):
    if pscan(x):
        # p=[]
        # p.append(x)
        print('Port',x, 'is open')
        
    else:
        print('Port',x, 'is closed')

# savefile=open('pm.txt', 'w')
# savefile.write(str(p))   

    

