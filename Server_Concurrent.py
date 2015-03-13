import threading
from threading import Thread
import time
import socket
import sys


def master1():
	global s1# = socket.socket()
	s1 = socket.socket()
	host = ''
	global port1# = 2222
	port1 = 2222
	s1.bind((host, port1))
	

	threads1 =[]
	for i in range(3):
		print("START")
		t11=threading.Thread(target=slave1)
		threads1.append(t11)
		t11.start()
	


def slave1():
	
	s1.listen(5)
	while True:
		c1, addr1 = s1.accept()
		print "GOT CONNECTION FROM",addr1
		print("After Receiving.......") 
		for i in range (30):
			a=int(c1.recv(2))
			print 'Number received : ', a , ' from ',addr1
			z=(a+10)
			time.sleep(1)
			c1.send(str(z))
			print 'Sending  : ', z, ' to ',addr1
			
	c1.close()

def master2():
	global s2 # = socket.socket()
	s2 = socket.socket()
	host = ''
	global port2 # = 2223
	port2 = 2223
	s2 = socket.socket()
	s2.bind((host, port2))



	threads2 =[]
	for i in range(3):
		print("START")
		t21=threading.Thread(target=slave2)
		threads2.append(t21)
		t21.start()
	
	
def slave2():

	s2.listen(5)
	while True:
		c2, addr2 = s2.accept()
		print "GOT CONNECTION FROM",addr2
		print("After Receiving.......") 
		for i in range (30):
			a=int(c2.recv(2))
			print 'Number received : ', a , ' from ',addr2
			z=(a*a)
			time.sleep(1)
			c2.send(str(z))
			print 'Sending  : ', z, ' to ',addr2
			
	c2.close()


def master3():
	global s3 # = socket.socket()
	s3 = socket.socket()
	host = ''
	global port3 # = 2224
	port3 = 2224
	s3.bind((host, port3))
	

	threads3 =[]
	for i in range(3):
		print("START")
		t31=threading.Thread(target=slave3)
		threads3.append(t31)
		t31.start()

def slave3():
	
	s3.listen(5)
	while True:
		c3, addr3 = s3.accept()
		print "GOT CONNECTION FROM",addr3
		print("After Receiving.......") 
		for i in range (30):
			a=int(c3.recv(2))
			print 'Number received : ', a , ' from ',addr3
			z=(a+a)
			time.sleep(1)
			c3.send(str(z))
			print 'Sending  : ', z, ' to ',addr3
			
	c3.close()

def master4():
	global s4 # = socket.socket()
	s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	host = ''
	#global port4 # = 8888
	#port4 = 8888
	listen_addr = ("",8888)
	s4.bind(listen_addr)
	print 'After bind'
	slave4()
	'''threads4 =[]
	for i in range(3):
		print("START")
		t41=threading.Thread(target=slave4)
		threads4.append(t41)
		t41.start()	'''


def slave4():

	print ('in slave4')
	while True:
		data,addr4 = s4.recvfrom (1024)
		print data.strip(), addr4
     
#s.close()
			
	s4.close()



t1 = Thread(target=master1, args=())
t2 = Thread(target=master2, args=())
t3 = Thread(target=master3, args=())
t4 = Thread(target=master4, args=())
t1.start()
t2.start()
t3.start()
t4.start()
