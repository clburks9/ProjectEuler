from EulerHelpers import *


ans = 1000000; 
cur = 20;
while(1>0): 
	cur = cur+20;
	flag = True;  
	for j in range(2,21):
		if(cur%j!=0):
			flag = False; 
			break;
	if(flag == True):
		ans = cur; 
		break; 
print("Answer: {}".format(ans)); 