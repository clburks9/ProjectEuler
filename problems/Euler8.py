from EulerHelpers import *
import numpy as np; 

dataStr = ''; 

with open("../data/Euler8Data.txt") as f:
	for line in f: 
		dataStr +=line; 

data = []; 
for s in dataStr:
	if(s.isdigit()):
		data.append(int(s)); 

numNums = 13; 

ans = 0; 
for i in range(0,len(data)-numNums):
	prod = 1; 
	for j in range(0,numNums):
		prod = prod*data[i+j]; 
	if(prod>ans):
		ans = prod; 

print("Answer: {}".format(ans)); 
