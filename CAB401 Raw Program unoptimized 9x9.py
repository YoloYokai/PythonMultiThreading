###
# Program writen By Joshua Rowley N10233121
###

import math
import time
quadrantList = [
	[[3,3],[3,6],[3,9]],
	[[6,3],[6,6],[6,9]],
	[[9,3],[9,6],[9,9]]]
global possible_nums
possible_nums = [1,2,3,4,5,6,7,8,9]


global suduko
suduko1 = [
[5,6,0,8,4,7,0,0,0],
[3,0,9,0,0,0,6,0,0],
[0,0,8,0,0,0,0,0,0],
[0,1,0,0,8,0,0,4,0],
[7,9,0,6,0,2,0,1,8],
[0,5,0,0,3,0,0,9,0],
[0,0,0,0,0,0,2,0,0],
[0,0,6,0,0,0,8,0,7],
[0,0,0,3,1,6,0,5,9]]


suduko1_2=[
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]]

suduko2 = [
[0,0,4,0,0,2,0,5,0],
[0,2,1,0,7,0,0,3,0],
[0,0,0,0,0,6,0,0,9],
[0,0,0,0,0,4,0,0,2],
[5,0,0,1,2,0,0,0,0],
[9,0,0,8,0,0,5,0,0],
[0,0,0,0,0,0,0,0,0],
[0,0,0,5,0,3,7,0,6],
[8,0,5,0,0,0,0,0,0]]

suduko = suduko1



def main():
	suduko = suduko1
	#printsoduko(suduko)
	i=26789
	start = time.time()
	while (zerocheck(suduko)>1 and i>1):
		output= [[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
		row= [[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]]]
		column= [[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]]]
		quadrant= [[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]],[[],[],[],[],[],[],[],[],[]]]


		for x in range(len(suduko[0])):
			for y in range(len(suduko)):
				new_value=0
				if(suduko[x][y]==0):
					row[x][y] = rows(suduko,x,y)
					column[x][y] = columns(suduko,x,y)
					quadrant[x][y] = quadrants(suduko,x,y)
				else:
					output[x][y]=suduko[x][y]	
		new_values = sames(row,column,quadrant,output)
		#new_values = unique_check(new_values)
		suduko=remove_lists(new_values)
		print(zerocheck(suduko))
		i=i-1

	end = time.time()
	print(str(end-start))

def printsoduko(matin):
	for y in range(len(matin)):
		for x in range(len(matin)):
			print(str(matin[x][y])+"|",end='')
		print('\n',end="")

def zerocheck(inputSuduko):
	output = 0
	for x in range(len(inputSuduko)):
		for y in range(len(inputSuduko)):
			if((inputSuduko[x][y]==0) or (type(inputSuduko[x][y]) is list)):
				output+=1
	return output

def rows(inputSuduko,x,y):
	output = []
	for i in range(len(inputSuduko)):
		if((inputSuduko[i][y]!=0) and (type(inputSuduko[i][y]) is not list)):
			#print(inputSuduko[i][y],end="")
			try:
				output.append(inputSuduko[i][y])
			except:
				continue;
	return output

def columns(inputSuduko,x,y):
	output = []
	# check column
	for i in range(len(inputSuduko)):
		if((inputSuduko[x][i]!=0) and (type(inputSuduko[x][i]) is not list)):
			#print(inputSuduko[x][i],end="")
			try:
				output.append(inputSuduko[x][i])
			except:
				continue;
	return output

def quadrants(inputSuduko,x,y):
	output = []
	quadrant = quadrantList[math.floor((x)/3)][math.floor((y)/3)]

	# check quadrant
	for xi in range(quadrant[0]-3,quadrant[0]):
		for yi in range(quadrant[1]-3,quadrant[1]):
			
			if((inputSuduko[xi][yi]!=0) and (type(inputSuduko[xi][yi]) is not list)):
				#print(inputSuduko[xi][yi],end="")
				try:
					output.append(inputSuduko[xi][yi])
				except:
					continue;
	return output




def remove_lists(input_arrary):
	output=input_arrary

	for x in range(len(output)):
		for y in range(len(output)):
			if(type(input_arrary[x][y]) is list):
				output[x][y]=0
	return(output)
	
def sames(a,b,c,d):
	output= [
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]]

	for x in range(len(a)):
		for y in range(len(a)):
			if(len(a[x][y])==0):
				output[x][y]=d[x][y]
			else:
				final = [1,2,3,4,5,6,7,8,9]
				for value in a[x][y]:
					if(value in final):
						final.remove(value)
				for value in b[x][y]:
					if(value in final):
						final.remove(value)
				for value in c[x][y]:
					if(value in final):
						final.remove(value)
				if(len(final)==1):
					print("x: "+str(x)+"  y: "+str(y)+" z: "+str(final))
					output[x][y]=final[0]
				else:
					output[x][y]=final
	return output
				



if __name__ == '__main__':
	main()

