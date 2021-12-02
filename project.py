class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items

def prioritize(a , b):
    if (a=='/' or a=='*') and (b=='/' or b=='*'):
        return False
    elif (a=='/' or a=='*') and (b=='+' or b=='-'):
        return True
    elif (a=='/' or a=='*') and (b=='^'):
        return True
    elif (a=='+' or a=='-') and (b=='+' or b=='-'):
        return False
    elif (a=='+' or a=='-') and (b=='^'):
        return True
    else:
        return False
def infix_to_postfix(userin):
    mystack = Stack()
    answer=[]
    for item in userin:
        if item==')':
            for i in mystack.get_stack():
                if  mystack.peek() =='(':
                    mystack.pop()
                    break
                else:
                    answer.append(mystack.pop())
        elif item=='(':
            mystack.push(item)

        elif item!='+' and item!='-' and item!='*' and item!='/' and item!='(' and item!=')' and item!='^':
            answer.append(float(item))

        else:
            if (mystack.is_empty() or prioritize(  item,mystack.peek())) and mystack.peek()!='(':
                mystack.push(item)
            elif mystack.peek()=='(':
                mystack.push(item)
            else:
                answer.append(mystack.pop())
                mystack.push(item)
    while not mystack.is_empty():
        answer.append(mystack.pop())
    return answer

def separate(userin):
    negetivs=0
    list_userin = []


    for item in userin:
        list_userin.append(item)


    for item in range(0,len(list_userin)):
        try:
            if list_userin[item]=='-' and list_userin[item+1]=='(':
                negetivs +=1
                list_userin.pop(item)
            elif list_userin[item]=='-' and list_userin[item-1]=='(' and list_userin[item+1].isdigit():
                string=''
                list_userin.pop(item)
                list_userin.pop(item-1)
                string='-'
                item -=1
                while list_userin[item]=='.'or list_userin[item].isdigit():
                    string += list_userin[item]
                    list_userin.pop(item)

                list_userin.insert(item,string) 
        except:
            pass

        try:
            #if list_userin[item].isdigit() and list_userin[item+1]==')' and list_userin[item-1]=='-'and list_userin[item-2]=='(':
#string=''
            #    string +=list_userin[item-1]
            #    string +=list_userin[item]
            #    list_userin.pop()
            #    list_userin.pop()
#list_userin.pop(item-1)
            #    list_userin.pop(item-1)
            if list_userin[item].isdigit():
                string=''
                while list_userin[item]=='.'or list_userin[item].isdigit():
                    string += list_userin[item]
                    list_userin.pop(item)

                list_userin.insert(item,string)                    
        except:
            pass
        

    list_userin.pop()
    

    return list_userin ,negetivs

def math(num1 , operator , num2):
    if operator == '^':
        return num1 **num2
    elif operator == '-':
        return num1 -num2
    elif operator == '+':
        return num1 +num2
    elif operator == '/':
        return num1 /num2  
    elif operator == '*':
        return num1 *num2  

def calculator(string ,  negetivs):
        tree = []

        item=0
        while (item< len(string)):
            if string[item]=='(':
                string.pop(item)
            item+=1
        item=0
        while (item< len(string)):
            try:
                if  (string[item+1]=='-' or string[item+1]=='+' or string[item+1]=='*' or string[item+1]=='/' or string[item+1]=='^'):
                    answer = math(string[item-1] ,string[item+1] , string[item] )
                    string.pop(item)
                    string.pop(item)
                    string.pop(item-1)
                    string.insert(item-1 , answer)
                    item=item-2
            except:
                pass

                
            item+=1
        if negetivs %2==0:
            return answer
        else:
            return answer*-1
userin='(1+3)*2^2'
a,b=separate( userin+',')

f=infix_to_postfix(a)
print(a)
print(b)
print(f)
print(calculator(f,b))

#--------------------------------------------------------------------------------------------------
#  Function			Description
#--------------------------------------------------------------------------------------------------
#  all()            Returns True if all the Boolean values in the list are True, else returns False
#  any()			Returns True if any of the Boolean values in the list is True
#  append()         Adds an item to the end of the list
#  len()			Returns the numbers of items in a list
#  insert()         Inserts an item at a given position
#  pop([])          Removes the item at the given position in the list
#  clear()          Removes all items from the list.           
#  reverse()        Reverses the elements of the list
#  sort()			Sorts the elements of the list.
#  min()            Returns the smallest item in the list.
#  max()            Returns the largest item in the list.
#--------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
#   name       			description
#-------------------------------------------------------------------------------------------
#   len()               Returns the number of characters in a string
#   capitalize()        Converts the first character of a string to capital letter
#   count()             Returns the number of occurrences of a substring in the given string
#   lower()             Converts a string into lower case
#   upper()	            Converts a string into upper case
#   isspace()           Returns True if all characters in the string are whitespaces
#   replace()           Replaces all or part of a string with another string
#   isdigit()           Returns True if the string consists of digits only
#-------------------------------------------------------------------------------------------
