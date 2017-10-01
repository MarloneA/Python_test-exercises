'''

#returns a sum of nested lists


def nested_sum(arg):
	
	index=[]
	for i in arg:
		#if type(i) == 'list':
			index.extend(i)

		#else:
		#	index.append(i)
	index.sort()
	print sum(index)


nested_sum([[2,3,4,5],[1,2,3,4],[6,7,8,9]])


#returns a list of capitalised arguments

def capitalise(arg):
	cap =[]
	
	for i in arg:
		cap.append(i.capitalize())

	print "".join(cap)



capitalise('the quick brown fox')


def capitalize_nested(arg):

	cap = []
	nested_cap=[]
	final_nest =[]

	for i in range(len(arg)):
		
		for j in arg[i]:
				nested_cap.append(j.capitalize())

		final_nest.append(nested_cap)

	cap.append(nested_cap)

	print cap

capitalize_nested([['p','a','r'],['a','m','o'],['r','e']])



def is_upper(word):
	arr=[]
	for l in word:
		if l.isupper():

			arr.append(l)

	print arr

is_upper('Andela')


def cummulative_sum(arg):

	cumm=[]
	total=0
	for i in arg:
		total +=i
		cumm.append(total)

	print cumm


cummulative_sum([1,1,1,1,1,1,1,1,1])




def middle(arg):

	del arg[0]

	del arg[len(arg)-1]

	print arg


middle([1,2,3,4])



def chop(arg):

	
	print arg.remove(arg[0]) ,arg.remove(arg[len(arg)-1])


chop([1,2,3,4])






#Exercise 10.6. 

#Write a function called is_sorted that takes a list as a parameter and 
#returns True if the list is sorted in ascending order and False otherwise. You can assume 
#(as a precondition) that the elements of the list can be compared with the relational 
#operators <, >, etc.
#For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) 
#should re- turn False.




def is_sorted(arg):

	new = arg[:]
	new.sort()
	if arg == new:
		print 'true'

	else:
		print 'false'


is_sorted(['d','e','a','c'])





#Exercise 10.7. 

#Two words are anagrams if you can rearrange the letters from one to spell the other.
# Write a function called is_anagram that takes two strings and returns True if they are 
# anagrams.


def is_anagram(word1, word2 ):

	new = list(word1)
	new.sort()

	new2 = list(word2)
	new.sort()

	if new == new2:

		print 'True'

	else:

		print 'False'


is_anagram('dady','add')




def has_duplicates(arg):



def recur(n):
	
	while n > 0:

		print 'shoobat', 'lemon','grand'
		n=n-1

recur(5)


def sequence(n):
    while n != 1:
        print n,
        
        if n%2 == 0:
			n = n/2 
		
		else:
			n = n*3+1

sequence(2)


#Collatze conjecture

def sequence(n):
	
	while n!= 1:
	
		print n,
	
		if n%2 ==0:
	
			n=n/2

		else:
			n= n*3+1


sequence(100)




while True:
     line = raw_input(' -  ')
     if line == 'done':
             break




def right_justify(arg):

	print  " "*70 , arg


right_justify('Marko')




def print_grid():

	print "+","-"*4,"+","-"*4,"+","-"*4,"+"
	print "|", " "*4,"|", " "*4,"|", " "*4,"|"
	print "|", " "*4,"|", " "*4,"|", " "*4,"|"
	print "|", " "*4,"|", " "*4,"|", " "*4,"|"
	print "|", " "*4,"|", " "*4,"|", " "*4,"|"

	print "+","-"*4,"+","-"*4,"+","-"*4,"+"
	print "|", " "*4,"|", " "*4,"|", " "*4,"|"
	print "|", " "*4,"|", " "*4,"|", " "*4,"|"
	print "|", " "*4,"|", " "*4,"|", " "*4,"|"
	print "|", " "*4,"|", " "*4,"|", " "*4,"|"

	print "+","-"*4,"+","-"*4,"+","-"*4,"+"


	print "|", " "*4,"|", " "*4,"|", " "*4,"|"
	print "|", " "*4,"|", " "*4,"|", " "*4,"|"
	print "|", " "*4,"|", " "*4,"|", " "*4,"|"
	print "|", " "*4,"|", " "*4,"|", " "*4,"|"

	print "+","-"*4,"+","-"*4,"+","-"*4,"+"

print_grid()




from math import sqrt

def hypotunese(b,c):

	sq = b**2
	sq2=c**2

	result = sq + sq2

	answ = sqrt(result)

	return answ

print hypotunese(8,6)



def is_between(x,y,z):
	

	 x>=y and x<=z:
		

is_between(2,1,3)



def fact(n):

	if n == 0 :
		return 1

	else:


		result = n*fact(n-1)

		return result


print fact(5)




def fibonacci(n):

	if n == 0:

		print 0

	elif n == 1:
		return 1

	else:
		return fibonacci(n-1) + fibonacci(n-2)

print fibonacci(10)




def factorial(n):
   
    space = ' ' * (4 * n)
   
    print space, 'factorial', n
   
    if n == 0:
   
        print space, 'returning 1'
   
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print space, 'returning', result
        return result


factorial(200)




def string_traversal_inverse(fruit):


	index = 1
	while index < len(fruit)+1:
	    letter = fruit[-index]
	    print letter
	    index = index + 1



string_traversal_inverse("apple")



def robert_mclausky():

	prefixes = "JKLMNOPQ"
	suffix = "ack"

	for i in prefixes:
		
		if i == "O" or i == "Q":
			print i + "u"+ suffix

		else:
			print i  + suffix


robert_mclausky()





def find(word, letter , index):
	
    
	while index < len(word):
        
		if word[index] == letter:
	            
			print letter
		index += 1
	return -1

find('andela', 'a', 1)






###########################   anagram  ##################################

def word_count(word):

	count = 0

	splice = word[:]

	for letter in word:

		if letter == splice[len(word)-1]:

		
			count += 1


	print letter, count


word_count('andela')



def is_anagram(word):

	for letter in word:

		if word.count(letter) >= 2:

			print letter
		

is_anagram('andela')

	



def word_comparason(word):

	count = 0
	while count < len(word)

		if word[count] == word[count+1]:

			return True

	



def fermat(a,b,c,n):

	if n <= 2 :

		return 'number should be greater than 2'

	else:
		

		res1 = a**n
		res2 = b**n

		res_right = c**n

		res_left = res1 + res2

		if res_left == res_right:

			return 'Holy smokes fermat was wrong'


		else:

			return 'nope that doesnt work'

		




def user():

	a=int(raw_input("Enter a :  "))
	b=int(raw_input("Enter b :  "))
	c=int(raw_input("Enter c :  "))
	n=int(raw_input("Enter n :  "))


	print fermat(a,b,c,n)



user()





def is_triangle(l1,l2,l3):

	sum1 = l1+l2
	sum2 = l1+l3
	sum3 = l2+l3

	if sum1 < l3 or sum2 < l2 or sum3 < l1:

		return 'sorry bro, no triangle for you'

	else:

		return 'yes, you have a triangle'

is_triangle(10,16,6)


def user():

	l1=int(raw_input("Enter l1 :  "))
	l2=int(raw_input("Enter l2 :  "))
	l3=int(raw_input("Enter l3 :  "))
	


	print is_triangle(l1,l2,l3)



user()


def reverse_lookup(d, v):
	
	for k in d:
	
		if d[k] == v:
	
			return k
	
	raise ValueError("Out of range")


print reverse_lookup({1:'a',2:'e',3:'i',4:'o',5:'u'},'z')






def reverse_lookup(d, v):
	
	keys_on_v=[]

	for k in d:
	
		if d[k] == v:
	
			keys_on_v.append(k)

			return keys_on_v

		
	
	return []


print reverse_lookup({1:'a',2:'e',3:'i',4:'o',5:'u'},'z')





def invert_dict(d):
	inverse = dict()
	for key in d:
		val = d[key]
		if val not in inverse:
			inverse[val] = [key]
		else:
			inverse[val].append(key)
	return inverse

print invert_dict({1:'a',2:'e',3:'i',4:'o',5:'u'})








#Create a method using Python 2.7.x syntax called is_isogram that takes one argument, 
#a word to test if it's an isogram. This method should return a tuple of the word and 
#a boolean indicating whether it is an isogram.

#If the argument supplied is an empty string, return the argument and False: (argument, False). I
#f the argument supplied is not a string, raise a TypeError with the message 'Argument should be a string'.

#Example:

#is_isogram("abolishment")
#Expected result:

#("abolishment", True)



def is_isogram(word):
    if type(word) != str:
        raise TypeError('Argument should be a string')

    elif word == "":
      return (word, False)
    else:
        word = word.lower()
        for char in word:
            if word.count(char) > 1:
                return (word, False)
            else:
                return (word, True)







#Create a class called ShoppingCart.

#Create a constructor that has no arguments and sets the total attribute to zero, 
#and initializes an empty dict attribute named items.

#Create a method add_item that requires item_name, quantity and price arguments. 
#This method should add the cost of the added items to the current value of total. 
#It should also add an entry to the items dict such that the key is the item_name and 
#the value is the quantity of the item.

#Create a method remove_item that requires similar arguments as add_item. 
#It should remove items that have been added to the shopping cart and are not required.
 #This method should deduct the cost of these items from the current total and also 
 #update the items dict accordingly. If the quantity of items to be removed exceeds 
 #current quantity in cart, assume that all entries of that item are to be removed.

#Create a method checkout that takes in cash_paid and returns the value of balance from the payment.
# If cash_paid is not enough to cover the total, return Cash paid not enough.

#Create a class called Shop that has a constructor which initializes an attribute called quantity at 100.

#Make sure Shop inherits from ShoppingCart.

#In the Shop class, override the remove_item method, such that calling 
#Shop's remove_item with no arguments decrements quantity by one.

#JavaScript

#use camel case for your class method names, such that

#    add_item 
#becomes

#    addItem 



class ShoppingCart(object):

    def __init__(self):
        self.total = 0
        self.items = dict()

    def add_item(self, item_name, quantity, price):
        if item_name != None and quantity >= 1:
            self.items.update({item_name: quantity})
        if quantity and price >= 1:
            self.total += (quantity * price)

    def remove_item(self, item_name, quantity, price):
        self.total -= (quantity * price)
        try:
            if quantity >= self.items[item_name]:
                self.items.pop(item_name, None)
            self.items[item_name] -= quantity
        except(KeyError, RuntimeError):
            pass

    def checkout(self, cash_paid):
        balance = 0
        if cash_paid < self.total:
            return "Cash paid not enough"
        balance = cash_paid - self.total
        return balance


class Shop(ShoppingCart):

    def __init__(self):
        self.quantity = 100

    def remove_item(self):
        self.quantity -= 1

,,,


































































