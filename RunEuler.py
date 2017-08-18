import os; 
import sys; 
import subprocess; 


while 1>0:
	
	num = 1; 
	try: 
		num = int(input('Which Project Euler program would you like to run?\n'))
	except ValueError:
		print("Not a number"); 
		
	to_run = "./problems/Euler{}.py".format(num);  
	
	execfile(to_run); 



