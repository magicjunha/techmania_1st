import socket
from threading import Thread

HOST = '10.171.24.87'
PORT = 9008

class Client:

   def rcvMsg(sock):
      while True:
         try:
            data = sock.recv(1024)
            if not data:
               break
            print(data.decode())
         except:
            pass

 

   def runChat():
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         sock.connect((HOST, PORT))
         t = Thread(target=rcvMsg, args=(sock,))
         t.daemon = True
         t.start()
 

         while True:
            msg = input()
            if msg == '/quit':
               sock.send(msg.encode())
               break
        
            sock.send(msg.encode())
           

   def SendData(self,message):
      with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
         sock.connect((HOST, PORT))
         sock.send(message.encode())
         a,b,c = message.split(';')
         msg = sock.recv(1024)
         print(msg.decode())
         sock.close()

#runChat()
