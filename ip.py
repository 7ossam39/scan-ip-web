import socket
import sys

print('Enter Your DNS or Target: ')
hostname = input()
ip=socket.gethostbyname(hostname)
print ('Host Name Is: ',hostname, '\n' 'Target Ip Is: ',ip)
input ('Press enter to Exit...')
