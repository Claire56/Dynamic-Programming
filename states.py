
# given a list of cells, active cells are labelled 1 and inactive 0, cells compete with
# their neighbors if both neighbors have same valuesthen the next day that cell will be inactive
# if they have different values then the next day that cell will be active. return state of cells after k days
#example listg = [0,1,0,1,0,1,0,1],k=1.   =>[1,0,0,0,0,0,0,0]



listg = [0,1,0,1,0,1,0,1]

def newstate(states,k):
	states=states
	n=len(states)
	states2=states

	while k>0:
		if states[0]==1 and states[1]==0:
			states2[0]=0

		elif states[0]==1 and states[1]==1:
			states2[0]=1
		if states[-1]==1 and states[-2]==0:
			states2[0]=0

		elif states[-1]==1 and states[-2]==1:
			states2[0]=1
		
		for i,v in enumerate(states[1:n-1]):
			if v == 1 and states[i-1]==states[i+1]:
				states2[i] = 0
				
			elif v==1 and states[i-1] != states[i+1]:
				states2[i] = 1
		newstate(states2,k-1)	   
		
print(newstate(listg,5))
