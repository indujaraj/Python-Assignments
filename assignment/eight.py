lst=[]
odd=[]
n=int(input(("enter no of elements")))
for i in range(n):
    e=int(input())
    lst.append(e)
for i in lst:
    if i%2!=0:
        odd.append(i)
odd.sort()
print(odd[0])