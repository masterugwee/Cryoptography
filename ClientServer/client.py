#Code done by Varun Nair(7h3M0nk)

import socket
from cryptography.fernet import Fernet
import hashlib
import hmac


def client_program():
    #key = Fernet.generate_key()
    key = b'ADH-_MMQf5LQH127Fo9VjYy6Z6IA69W0_z-c40-h2Wk='                 # I generated a key and using it for both client and server. Better than sending a key everytime. More secure.
    f = Fernet(key)
    hmackey = "7h3M0nkIstheOwnerofthisProgram"                      #Key for the hmac

    #print(key)
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    message = ''


    while message.lower().strip() != 'bye':
        message = input(" -> ")  # take input
        senddigest = hmac.new(hmackey.encode(),message.encode(),hashlib.sha512)              #Creating a hexdigest to be sent.
        token = [f.encrypt(str.encode(message)),hashlib.sha512(message.encode()).hexdigest(),senddigest.hexdigest()]                      #a hashlib sha512 is also in the list.
        token = str(token)
        client_socket.send(str.encode(token))  # send message
        data = client_socket.recv(1024).decode()  # receive response
        data = (data.split(','))
        #senderkey = str(data[3])[3:-1]
        clienthmac = str(data[2][2:-2])
        #print(data[1])
        #f2 = Fernet(key)
        clientmessage = (f.decrypt(str(data[0])[3:-1].encode())).decode()               #Convert the client message to string.
        print('Received from server: ' ,clientmessage)  # show in terminal
        if (str(data[1])[2:-1]) == str(hashlib.sha512(f.decrypt(str(data[0])[3:-1].encode())).hexdigest()):                  #Checking the hexdigest of the sender with the message received
            print("Message is from the sender.sha512 confirmed")
        hexdigesthmac = hmac.new(hmackey.encode(),clientmessage.encode(),hashlib.sha512)              #generated an hmac
        if(clienthmac == hexdigesthmac.hexdigest()):                                 #checking the hmac hex hexdigest is the same.
            print("Hmac verified")
        #message = input(" -> ")  # again take input

    client_socket.close()  # close the connection.


if __name__ == '__main__':
    client_program()
