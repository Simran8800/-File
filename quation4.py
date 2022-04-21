a=open("quation4.txt","r")
f=a.read()
i=0
while i<len(a):
    if a[i]=="delhi":
        print("y")
    elif a[i]=="shimla":
        print("n")
    else:
        print("o")
a.close()
    