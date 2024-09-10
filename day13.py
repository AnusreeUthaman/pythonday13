
#FUNCTIONS

def greet(name,place):
    print(f"Name:{name}")
    print(f"place:{place}")
greet("anu","kannur")
#Name:anu
#place:kannur

greet("kannur","anu")#postional arguments
#Name:kannur
#place:anu

greet(place="kannur",name="anu")#keyword arguments
#Name:anu
#place:kannur




def add(x,y):
    return x+y
a=int(input("enter a number:"))
b=int(input("enter a number:"))
result=add(a,b)
print(result)#enter a number:4
             #enter a number:5
             #9


def elder(x,y,z):
    if x>y and y>z:
        return x
    elif y>z:
        return y
    else:
        return z
a=10
b=15
c=5
result=elder(a,b,c)
print(f"The elder one age is {result}")#The elder one age is 15
    

         
#default parameters-(at end)
def greet(name,place="india"):
    print(f"name:{name}")
    print(f"place:{place}")
greet("anusree")#name:anusree
                #place:india

greet("anu","delhi")#name:anu
                    #place:delhi



#Arbitary postional arguments-(*) type-tuples,
def sqr_sum(*numbers):#*args
    print(type(numbers))#<class 'tuple'>
    print(numbers)#(1, 2, 3)
    total=0
    for i in numbers:
        total+=i**2
    return total
print(sqr_sum(1,2,3))#14


def sqr_total(*numbers):
    sqr_sum=0
    for i in numbers:
        sqr_sum+=i**2
    return sqr_sum
print(sqr_total(7,5,3,4,5,6,8))#224
    




#Arbitary keyword arguments-(**)type-dict,

def student(**kwargs):
    print(kwargs)#{'name': 'abu', 'roll_no': 2, 'place': 'kochi'}
    print(type(kwargs))#<class 'dict'>
    for i in kwargs.keys():
        print(i)#name
                #roll_no
                #place
    for i in kwargs.values():
        print(i)#abu
                #2
                #kochi
    for i in kwargs.items():
        print(i)#('name', 'abu')
                #('roll_no', 2)
                #('place', 'kochi')
        
    for i in kwargs:
            print(i)#name
                    #abu
                    #roll_no
            print(kwargs[i])#2
                            #place
                            #kochi
    
    for i,j in kwargs.items():
        print(i,j)#name abu
                  #roll_no 2
                  #place kochi
    
student(name="abu",roll_no=2,place="kochi")



#no change in order
#postional arguments after keyword arguments

def data(*args,**kwargs):
    print(args)#(1, 2, 3)
    print(kwargs)
data(1,2,3,x=10,y=13)#{'x': 10, 'y': 13}

def data(*args,**kwargs):
    print(args)
    print(kwargs)
    
data(1,2,3,name="hello",place="calicut")#(1, 2, 3)
                                        #{'name': 'hello', 'place': 'calicut'}

data(1,2,3,4)#(1, 2, 3, 4)
            #{}  
data(x=10,y=12,z=13)#()
                    #{'x': 10, 'y': 12, 'z': 13}
data(w=12,q=13,35,45)


x="12345"
print(x.split(","))#['12345']
print(x)#12345




def find_avg(x):
    total=sum(x)
    length=len(x)
    return total/length
data=[1,2,3,4,5]
result=find_avg(data)
print(f"The average is: {result}")#The average is: 3.0



def find_avg(lst):
    total=0
    for i in lst:
        total+=i
    return total/len(lst)
data=[1,2,3,4,5]
print(find_avg(data))#3.0

