#Code done by Varun Nair(7h3M0nk) AM.SC.P2CSC19035.


import socket
from cryptography.fernet import Fernet
import hashlib
import hmac


def server_program():
    #key = Fernet.generate_key()
    key = b'ADH-_MMQf5LQH127Fo9VjYy6Z6IA69W0_z-c40-h2Wk='                 # I generated a key and using it for both client and server. Better than sending a key everytime. More secure.

    f = Fernet(key)
    hmackey = "7h3M0nkIstheOwnerofthisProgram"                     #Key for the hmac.
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port no above 1024


    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)

    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        data = (data.split(','))
        #senderkey = str(data[3])[3:-1]
        clienthmac = str(data[2][2:-2])
        #print(senderkey.encode())
        #print(str(data[0])[3:-1])
        #senderkey = base64.b64encode(bytes(data[1],'utf-8'))
        #print(str(data[1])[2:-1])
        #f2 = Fernet(senderkey.encode())
        #print(str(hashlib.sha512(f2.decrypt(str(data[0])[3:-1].encode())).hexdigest()))
        clientmessage = (f.decrypt(str(data[0])[3:-1].encode())).decode()                                         #Convert the client message to string.
        print("from connected user: " ,clientmessage)
        if (str(data[1])[2:-1]) == str(hashlib.sha512(f.decrypt(str(data[0])[3:-1].encode())).hexdigest()):              #Checking the hexdigest of the sender with the message received
            print("Message is from the sender.sha512 confirmed")
        hexdigesthmac = hmac.new(hmackey.encode(),clientmessage.encode(),hashlib.sha512)                                  #generated an hmac
        if(clienthmac == hexdigesthmac.hexdigest()):                                          #checking the hmac hex hexdigest is the same.
            print("Hmac verified")
        data = input(' -> ')
        senddigest = hmac.new(hmackey.encode(),data.encode(),hashlib.sha512)                        #creating a hex digest for the message

        token = [f.encrypt(str.encode(data)),hashlib.sha512(data.encode()).hexdigest(),senddigest.hexdigest()]             #Converting everything to a list also a sha512 is also included.
        token = str(token)         #converting to string

        conn.send(str.encode(token))  # send data to the client

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
