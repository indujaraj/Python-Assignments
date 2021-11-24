lst = list(map(int, input("Enter comma separated values: ").split(",")))
one=[]
tup=()
for i in lst:
    one.append(i)
for i in lst:
    tup+=(i,)

print(one)
print(tup)