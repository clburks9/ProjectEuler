import numpy as np; 


dataStr = []; 

with open("../data/Euler11Data.txt") as f:
	for line in f: 
		dataStr.append(line); 

data = np.zeros(shape=(20,20)).tolist(); 

for i in range(0,20):
	for j in range(0,20): 
		data[i][j] = int(dataStr[i][j*3:j*3+2]);


ans = 0; 

#horizontals
for i in range(0,20):
	for j in range(0,20-4):
		test = 1; 
		for k in range(0,4):
			test=test*data[i][j+k]; 
		if(test>ans):
			ans = test;

#verticals
for i in range(0,20-4):
	for j in range(0,20):
		test = 1; 
		for k in range(0,4):
			test=test*data[i+k][j]; 
		if(test>ans):
			ans = test; 

#diagonals
for i in range(0,20):
	for j in range(0,20):
		test = 1; 
		for k in range(0,4):
			if(i+k<20 and j+k<20):
				test=test*data[i+k][j+k]; 
		if(test>ans):
			ans = test;

#off diagonals
for i in range(4,20):
	for j in range(0,20):
		test = 1; 
		for k in range(0,4):
			if(i+k<20 and j+k<20):
				test=test*data[i-k][j+k]; 
		if(test>ans):
			ans = test;  

print("Answer: {}".format(ans)); 
