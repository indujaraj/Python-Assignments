tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tup1 = ()
for i in tuple:
    if i % 2 == 0:
        tup1 += (i,)

print(tup1)
