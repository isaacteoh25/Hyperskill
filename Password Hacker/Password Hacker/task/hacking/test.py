import random
from itertools import permutations
abc = 'abcd'
def random_password():
    '''function - generating random password of length from 2 to 3'''
    return ''.join(random.choice(abc) for i in range(random.randint(2, 3)))

passw= random_password()

count = 1
while True:
    your_list = 'abcdefghijklmnopqrstuvwxyz1234567890'
    my_iter = []
    for current in range(count):
        a = [i for i in your_list]
        for y in range(current):
            a = [x + i for i in your_list for x in a]
        my_iter = my_iter + a
    # my_iter = list(permutations(your_list, count))
    if passw in my_iter:
        print(passw)
        print(my_iter)
        break
    count = count + 1


# write your code here
# import sys
# import socket
#
# hostname = sys.argv[1]
# port = int(sys.argv[2])
# data = sys.argv[3]
# address = (hostname, port)
#
# # Create a new socket.
# client_socket = socket.socket()
#
# # Connect to a host and a port using the socket.
# client_socket.connect(address)
#
# # Send a message from the third command line argument to the host using the socket.
# password = data.encode()
# client_socket.send(password)
#
# # Receive the server’s response.
# response = client_socket.recv(1024)
# # decoding from bytes to string
# response = response.decode()
#
# # Print the server’s response.
# print(response)
#
# # Close the socket.
# client_socket.close()
