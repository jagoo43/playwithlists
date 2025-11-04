list1=[]
total=0
print("enter 10 numbers")
for i in range(1,11):
    list1.append(int(input()))
for i in list1:
    total=total+i
avg=total/10
print(total)  
print(avg)  
