f1=open("new.txt",'r')
count={}
for i in f1:
    word=i.rstrip("/n").split(" ")
    for j in word:
        if j not in count:
            count.update({j:1})
        else:
            value=count[j]
            value+=1
            count.update({j:value})

print(count)