from EulerHelpers import *

ans = 0; 

for i in xrange(2,600851475143):
	#is factor
	if(600851475143%i==0):
		tmp = 600851475143/i; 
		if(isPrime(tmp)):
			ans = tmp; 
			break;  

print("Answer:{}".format(ans)); 