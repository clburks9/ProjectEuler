

suma = 0; 
prev = 1; 
cur = 1; 
while(cur<4e6):
	tmp = cur; 
	cur = cur+prev;
	prev = tmp; 
	if(cur%2==0):
		suma+=cur; 
print("Answer: {}".format(suma)); 