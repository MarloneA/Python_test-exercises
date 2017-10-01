#python exercises from github 

########### Level 1: Questions ###########
'''
#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

def divisibility():

	stor =[]
	for number in range(2000,3201): 

		if number%7 == 0 and number%5 != 0:
			stor.append(str(number))


	print ','.join(stor)


divisibility()



#Question:
#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#40320

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.


def fact(x):

	

	if x == 0:

		return 1

	else:

		return x*fact(x-1)

x = int(raw_input("Please Enter a number  \n >>> "))

print fact(x)




#Question:
#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

#Hints:
#In case of input data being supplied to the question, it should be assumed to be a console input.
#Consider use dict()



def dic_generator():

	n = int(raw_input("Insert number constructor \n >>> "))

	gen = {x:x*x for x in range(1,n+1)}

	print gen


dic_generator()


######   alternative

#n=int(raw_input())
#d=dict()

#for i in range(1,n+1):
 #   d[i]=i*i

#print d




#Question:
#Write a program which accepts a sequence of comma-separated numbers from console 
#and generate a list and a tuple which contains every number.
#Suppose the following input is supplied to the program:
#34,67,55,33,12,98
#Then, the output should be:
#['34', '67', '55', '33', '12', '98']
#('34', '67', '55', '33', '12', '98')

#Hints:
#In case of input data being supplied to the question, it should be assumed to 
#be a console input.
#tuple() method can convert list to tuple

def raw():
	lis =[]

	for i in range(6):
		x=raw_input('>>> ')

		lis.append(x)

	print lis
	print tuple(lis)

raw()

'''

#Question:
#Define a class which has at least two methods:
#getString: to get a string from console input
#printString: to print the string in upper case.
#lso please include simple test function to test the class methods.

#Hints:
#Use __init__ method to construct some parameters


class ClassName(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		











