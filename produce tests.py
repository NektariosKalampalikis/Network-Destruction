import random

number=int(input("how many lines:"))
mylist=[]
while len(mylist)<number:
    x=random.randint(1,10)
    y=random.randint(1,10)
    while x==y:
        x=random.randint(1,100)
        y=random.randint(1,100)
    while (x,y) in mylist:
        x=random.randint(1,100)
        y=random.randint(1,100)
    while (y,x) in mylist:
        x=random.randint(1,100)
        y=random.randint(1,100)        
    mylist.append( (x,y))

myfile=open("example_1.txt","w")
for line in mylist:
    myfile.write(str(line[0])+" "+str(line[1])+"\n")
myfile.close()
