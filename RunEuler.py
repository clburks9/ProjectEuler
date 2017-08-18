import os; 
import sys; 
import subprocess; 


while 1>0:
	
	num = 1; 
	try: 
		num = int(input('Which Project Euler program would you like to run?\n'))
	except ValueError:
		print("Not a number"); 
		
	to_run = "./Problems/Euler"+str(num);  
	#print(to_run); 

	try:
		pm = __import__(to_run);
	except ImportError:
		print("Not a valid file"); 



