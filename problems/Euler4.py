from EulerHelpers import *

ans = 0; 
for i in xrange(999,900,-1):
	for j in xrange(999,900,-1):
		if(isPalli(i*j)):
			ans = i*j;
			print(i,j);  
			break; 
	if(ans!=0):
		break; 
print("Answer: {}".format(ans)); 