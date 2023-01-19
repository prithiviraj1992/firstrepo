import socket
import sys

global ipaddress
ipaddress = "10.237.131.32"
global port
port = 23

def setvalue(command):
	data1 = bytes(command, 'ascii')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ipaddress,port))
	s.send(data1)
	s.close()

def getvalue(command):
	data1 = bytes(command, 'ascii')
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ipaddress,port))
	s.send(data1)
	string = ""

	while True:
		# for m in range (0,20): #Disconnects after x chars
		data = s.recv(1) #Receive data from the socket.
		string += data.decode("utf-8")
		if "\n" in string:
			break
	s.close()
	print (string)
	return string
	
def main():
	setvalue('^TEMP SP 350$')
	getvalue('^TEMP SP?$')

	
if __name__ == '__main__':
    main()
