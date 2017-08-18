from EulerHelpers import *



numPrime = 0; 

count = 2; 
ans = 0; 
while(1>0):
	if(isPrime(count)):
		numPrime +=1; 
		if(numPrime==10001):
			ans = count; 
			break; 
	count = count+1;

print("Answer: {}".format(ans)); 