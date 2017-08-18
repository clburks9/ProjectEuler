from EulerHelpers import *

maxi = int(2e6);

ans = 0; 
for i in range(2,maxi):
	if(isPrime(i)):
		ans+=i; 


print("Answer: {}".format(ans)); 