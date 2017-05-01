import random

def testGame(n):
	stay = 0
	switch = 0
	for ii in range(n):
		choices = [0,0,1]
		random.shuffle(choices)
		guess = random.randrange(3)
		res = choices[guess]
	
		for i in choices:
			if i == 0:
				del(choices[i])
				break
			
		if res == 0:
			switch +=1
		else:
			stay +=1
			
	print("Probability to win on staying = {}".format(stay/n))
	print("Probability to win on switch = {}".format(switch/n))
	
prob = testGame(100000)