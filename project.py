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
    print(answer)

def separate(userin):
    negetivs=0
    list_userin = []


    for item in userin:
        list_userin.append(item)


    for item in range(0,len(list_userin)):
        try:
            if list_userin[item]=='-' and list_userin[item+1]=='(':
                negetivs +=1
                print(list_userin.pop(item))
                
        except:
            pass

        try:
            if list_userin[item].isdigit() and list_userin[item+1]=='.' and list_userin[item+2].isdigit():
                string=str(list_userin[item]+list_userin[item+1]+list_userin[item+2])
        
                list_userin.pop(item)
                list_userin.pop(item)
                list_userin.pop(item)

                list_userin.insert(item ,string )
                item-=1
        except:
            pass


    return list_userin ,negetivs


userin='6*-(2+3)'
a,b=separate( userin)
print(a)
infix_to_postfix(a)


