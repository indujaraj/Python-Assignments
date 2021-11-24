
def post(*args):
    a=args

    if(len(a)==0):
        print("Nobody likes this")
    if(len(a)==1):
        print(a[0],"likes this")
    if(len(a)==2):
        print(a[0],"and",a[1],"likes this")
    if(len(a)==3):
        print(a[0],",",a[1],"and",a[2],"likes this")
    if(len(a)==4):
        print(a[0],",",a[1],"and",len(a)-2,"others likes this")

post("Alice","Bob","Charly")