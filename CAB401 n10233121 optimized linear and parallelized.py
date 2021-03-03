###
# Program writen By Joshua Rowley N10233121
###




import math
import time
import csv
import logging
import threading
import time
import multiprocessing

from math import sqrt

def linear(suduko):
	start = time.time()
	lastloop=-1
	i=0
	print("linear")

	while zerocheck(suduko)>0 and zerocheck(suduko)!= lastloop:
		i = i+1
		lastloop = zerocheck(suduko)
		changes = []
		for x in range(len(suduko)):
			for y in range(len(suduko)):
				if((suduko[x][y]==-1) or (type(suduko[x][y]) is list)):
					new_value = calculate(suduko,x,y)
					if(new_value!=-1):
						suduko[x][y] = new_value
					else:
						suduko[x][y] = -1
		print(str(time.time()-start))
	
	print(str(time.time()-start))
	if(zerocheck(suduko)== lastloop):
		print("failed to completely fillout")
		print(f"completed {i} iterations")
	return suduko

def zerocheck(inputSuduko):
	output = 0
	for x in range(len(inputSuduko)):
		for y in range(len(inputSuduko)):
			if((inputSuduko[x][y]==-1) or (type(inputSuduko[x][y]) is list)):
				output+=1
	return output

def calculate(inputSuduko,x,y):

	quadrant = [int((math.floor((x)/sqrt(len(inputSuduko)))+1) * sqrt(len(inputSuduko))),
				int((math.floor((y)/sqrt(len(inputSuduko)))+1) * sqrt(len(inputSuduko)))]

	possible_nums = list(range(0,len(inputSuduko)))

	# check column
	for i in range(len(inputSuduko)):
		if((inputSuduko[x][i]!=-1) and (type(inputSuduko[x][i]) is not list)):
			try:
				possible_nums.remove(inputSuduko[x][i])
			except:
				continue;

	# check rows
	for i in range(len(inputSuduko)):
		if((inputSuduko[i][y]!=-1) and (type(inputSuduko[i][y]) is not list)):
			try:
				possible_nums.remove(inputSuduko[i][y])
			except:
				continue;

	# check quadrant
	for xi in range(quadrant[0]-int(sqrt(len(inputSuduko))),quadrant[0]):
		for yi in range(quadrant[1]-int(sqrt(len(inputSuduko))),quadrant[1]):
			if((inputSuduko[xi][yi]!=-1) and (type(inputSuduko[xi][yi]) is not list)):
				try:
					possible_nums.remove(inputSuduko[xi][yi])
				except:
					continue;

	if(len(possible_nums)==1):
		return possible_nums[0]
	else:
		return -1

def threadingcalc(suduko,start,end,q):
	tempt = suduko
	for x in range(start,end):
		for y in range(len(suduko)):
			if((suduko[x][y]==-1) or (type(suduko[x][y]) is list)):
				new_value = calculate(suduko,x,y)
				if(new_value!=-1):
					tempt[x][y] = new_value
				else:
					tempt[x][y] = -1
	output=[]
	for a in range(start,end):
		output.append(tempt[a])
	output.append([start,end])
	q.put(output)	


#takes sudoku puzzle input, and process count
def threadingmeth(inputsuduko,tot_processes):
	threadingoutput = [None] * len(inputsuduko)
	starta = time.time()
	#print(starta)
	lastloop=-1
	i=0
	print(f"total Processes {tot_processes}")
	while zerocheck(inputsuduko)>0 and zerocheck(inputsuduko)!= lastloop:
		i= i+1
		#print(zerocheck(inputsuduko))
		lastloop = zerocheck(inputsuduko)
		q = multiprocessing.Queue()
		rets=[]
		Processes = list()
		
		for index in range(tot_processes):
			start = int(index * int(sqrt(len(inputsuduko)))*(len(inputsuduko)/(tot_processes*15)))
			end = int(start + int(sqrt(len(inputsuduko)))*(len(inputsuduko)/(tot_processes*15)))
			x = multiprocessing.Process(target=threadingcalc, args=(inputsuduko,start,end,q))
			Processes.append(x)
			x.start()


		for p in Processes:
			ret = q.get()
			rets.append(ret)
		for p in Processes:
			p.join()
		
		for a in range(len(rets)):
				inputsuduko[rets[a][int(len(inputsuduko)/tot_processes)][0]:rets[a][int(len(inputsuduko)/tot_processes)][1]] = rets[a][0:int(len(inputsuduko)/tot_processes)]

		#print(len(inputsuduko))
		#print(len(inputsuduko[0]))
		print(str(time.time()-starta))
		
	#enda = time.time()
	#print(enda)
	#print(str(time.time()-starta))
	if(zerocheck(inputsuduko)== lastloop):
		#print("failed to completely fillout")
		print(f"completed {i} iterations")
	return inputsuduko
   


def checkequal(in1,in2):
	total = 0
	for x in range(len(in1)):
			for y in range(len(in1)):
				if(in1[x][y]!=in2[x][y]):
					total +=1
	print(f"total incorrect values {total}")

def load():
	with open('rawdata.csv', newline='') as csvfile:
		spamreader = csv.reader(csvfile)
		bigout=[]
		for row in spamreader:
			smallout=[]
			for value in row:
				if(value=="   "):
					smallout.append(-1)
				else:
					smallout.append(int(value))
			bigout.append(smallout)
	return bigout


if __name__ == '__main__':

	lineardata = linear(load())
	multidata1 = threadingmeth(load(),1)
	multidata3 = threadingmeth(load(),3)
	multidata5 = threadingmeth(load(),5)
	multidata9 = threadingmeth(load(),9)
	multidata15 = threadingmeth(load(),15)

	checkequal(lineardata,multidata1)
	checkequal(lineardata,multidata3)
	checkequal(lineardata,multidata5)
	checkequal(lineardata,multidata9)
	checkequal(lineardata,multidata15)

