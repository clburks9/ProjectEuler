import numpy as np; 

def isPrime(a):
	if(a<2):
		return True;
	if(a != 2 and a%2==0):
		return False; 

	for i in range(2,int(np.sqrt(a))+1):
		if(a%i==0):
			return False; 
	return True; 


def isPalli(a):
	if(isinstance(a,int)):
		a = str(a); 

	if(len(a)%2==0):
		if(a[0:len(a)/2] == a[len(a)/2:][::-1]):
			return True; 
	else:
		if(a[0:len(a)/2+1] == a[len(a)/2:][::-1]):
			return True; 
	return False; 



def factorial(a):
	suma = 1; 
	for i in range(1,a+1):
		suma = suma*i; 
	return suma; 