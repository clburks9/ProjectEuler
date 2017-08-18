import numpy as np; 



maxi = 1000; 

ans = 0; 
breakFlag = False; 
for a in range(1,1000):
	for b in range(1,1000):
		for c in range(max(a,b),1000-a):
			if(a**2+b**2 == c**2 and a+b+c == 1000):
				ans = a*b*c; 
				breakFlag = True; 
			if(breakFlag):
				break; 
		if(breakFlag):
			break; 
	if(breakFlag):
		break; 
print("Answer: {}".format(ans)); 
