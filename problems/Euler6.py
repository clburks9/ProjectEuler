from EulerHelpers import *


suma1 = 0; 
for i in range(0,101):
	suma1+= i**2; 
suma2 = 0; 
for i in range(0,101):
	suma2 += i; 
suma2 = suma2**2; 

ans = suma2-suma1; 

print("Answer: {}".format(ans)); 

