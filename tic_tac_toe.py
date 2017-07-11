#Tic_tac_toe

#widht/height must be odd
#Width must be a number n such that n-2%3=0
def create_grid(width,p_0,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8):
	sb=int((width-2)/3)
#	print(sb) 
	print(" " *int(sb) + str(p_0) +" "*int(sb) + "|" +  " " *int(sb) + str(p_1) + " "*int(sb) + "|" + " "*int(sb) + str(p_2) + " "*int(sb) ) 
	print("—"*(sb*2+1) + "+" + "—"*(sb*2+1) + "+" +  "—"*(sb*2+1))
	print(" " *int(sb) + str(p_3) +" "*int(sb) + "|" +  " " *int(sb) + str(p_4) + " "*int(sb) + "|" + " "*int(sb) + str(p_5) + " "*int(sb) ) 
	print("—"*(sb*2+1) + "+" + "—"*(sb*2+1) + "+" +  "—"*(sb*2+1))
	print(" " *int(sb) + str(p_6) +" "*int(sb) + "|" +  " " *int(sb) + str(p_7) + " "*int(sb) + "|" + " "*int(sb) + str(p_8) + " "*int(sb) ) 

p_dict={}

p_0=1
p_1=2
p_2=3
p_3=4
p_4=5
p_5=6
p_6=7
p_7=8
p_8=9
p_dict[p_0]=1
p_dict[p_1]=2
p_dict[p_2]=3
p_dict[p_3]=4
p_dict[p_4]=5
p_dict[p_5]=6
p_dict[p_6]=7
p_dict[p_7]=8
p_dict[p_8]=9
player_symbol="X"
computer_symbol="O"

def CheckVictory(p_0,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8):
	if p_0==p_1==p_2 or p_3==p_4==p_5 or p_6==p_7==p_8 or p_0==p_3==p_6 or p_1==p_4==p_7 or p_2==p_5==p_8 or p_0==p_4==p_8 or p_2==p_4==p_6:
		return True	
def ComputerMove(turn,p_0,p_1,p_2,p_3,p_4,p_5,p_6,p_7,p_8):
	if turn==0 and p_4!= player_symbol and p_0 or p_2 or p_6 or p_8:
		p_dict[p_4]=computer_symbol
	else:
		print("no move") 

end_game=False
turn=0
while end_game==False:
#	p_dict[p_0]="O"
	create_grid(5,p_dict[p_0],p_dict[p_1],p_dict[p_2],p_dict[p_3],p_dict[p_4],p_dict[p_5],p_dict[p_6],p_dict[p_7],p_dict[p_8])
	if CheckVictory(p_dict[p_0],p_dict[p_1],p_dict[p_2],p_dict[p_3],p_dict[p_4],p_dict[p_5],p_dict[p_6],p_dict[p_7],p_dict[p_8])==True:
		print("Good Game")
		end_game=True
	move=None 
	while end_game==False:
		move=input("Type a number to make a move:")
		try:
			move=int(move) 
			if move>0 and move <10 and p_dict[eval("p_"+str(move-1))]!=computer_symbol:
				break
			else:
				print("an integer 1-9 in an empty slot")
		except ValueError:
			print("an integer 1-9")
#		else:
#			print("an integer 1-9")
	if end_game==False:
		location_of_change="p_"+str(move-1)
		p_dict[eval(location_of_change)]=player_symbol
	ComputerMove(turn,p_dict[p_0],p_dict[p_1],p_dict[p_2],p_dict[p_3],p_dict[p_4],p_dict[p_5],p_dict[p_6],p_dict[p_7],p_dict[p_8])
	turn=turn+1
	
#	print(p_dict[eval(location_of_change)])
#	print (location_of_change)
#	print(type(location_of_change))


