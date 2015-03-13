import socket 
import time 
import threading 
import sys


host = '' 
ch=0


while ch!=3:
	print ('Enter your choice: ')
	print ('\n1. TCP\n2. UDP\n3. Exit')
	ch = int(input())
	
	if ch==1:
		#s=socket.socket()
		#port = 2222     
		#s.connect((host, port))

		print ('Enter service to avail: ')
		print ('\n1. Add 10\n2. Square\n3. Double')
		ch1 = int(input())

		if ch1==1:
			s=socket.socket()
			port = 2222     
			s.connect((host, port))


			print("Enter a value to send: ")
			a = input() 
			s.send(str(a))



			for i in range (30):
				print 'Sent : ', i
				s.send(str(i))
				time.sleep(1)
				q=int(s.recv(2))
				q1=int(q)
				print 'Received : ', q
			s.close()


		elif ch1==2:
			s=socket.socket()
			port = 2223
			s.connect((host, port))


			print("Enter a value to send: ")
			a = input() 
			s.send(str(a))



			for i in range (30):
				print 'Sent : ', i
				s.send(str(i))
				time.sleep(1)
				q=int(s.recv(4))
				q1=int(q)
				print 'Received : ', q
			s.close()



		elif ch1==3:
			s=socket.socket()
			port = 2224 
			s.connect((host, port))


			print("Enter a value to send: ")
			a = input() 
			s.send(str(a))



			for i in range (30):
				print 'Sent : ', i
				s.send(str(i))
				time.sleep(1)
				q=int(s.recv(2))
				q1=int(q)
				print 'Received : ', q
			s.close()

		elif ch1!=1 or ch1!=2 or ch1!=3:
			break;



	elif ch==2:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		#port = 8888;

		while True:
			print ('Enter the string you wish to send: ')
			data = raw_input()
		
			addr4 = ("", 8888)
			s.sendto (data,addr4)

		s.close()





