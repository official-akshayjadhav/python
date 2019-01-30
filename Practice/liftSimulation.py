floors = [0,1,2,3,4,5,6,7]
lift = 0

while(True):
	inp = int(input("enter floor number: "))
	if(inp == -1):
		break
	if(inp > lift):
		print("lift going from-to: ", "->".join(str(e) for e in floors[lift: inp+1]))
		lift = inp
	else:
		if(inp == 0): print("lift going from-to: ", "->".join(str(e) for e in floors[lift::-1]))
	
		else: print("lift going from-to: ", "->".join(str(e) for e in floors[lift:inp-1:-1]))
		lift = inp
 
