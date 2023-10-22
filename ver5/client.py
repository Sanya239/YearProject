import socket
import time

# create TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# retrieve local hostname
local_hostname = socket.gethostname()

# get fully qualified hostname
local_fqdn = socket.getfqdn()



# bind the socket to the port 23456, and connect
def client_online(parent):
    ip_address  = parent.ip_asker.text2
    server_address = (ip_address, 5000)
    sock.connect(server_address)
    print("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))

    # define example data to be sent to the server
    while parent.turn_number>0:
        try:
            # show who connected to us
            data = tuple(str(sock.recv(1024)).split(' '))
            parent.turn(data)
            turn = parent.turn_number
            i = 20
            # receive the data in small chunks and print it
            while i >= 0:
                parent.parent.update()
                i -= 1

        finally:
            # Clean up the connection
            sock.send(bytes(str(parent.last_turn[0]) + ' ' + str(parent.last_turn[1])))
            sock.close()

    # close connection
    sock.close()