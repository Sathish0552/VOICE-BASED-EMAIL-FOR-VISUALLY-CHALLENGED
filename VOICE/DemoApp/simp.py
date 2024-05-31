pas=input()
z=list(pas)
res = ""
count=0
for i in z:
    if (i != " "):
        res = res + i
        count=count+1
    if(count==4):
        res=res+" "
        count=0
print(res)