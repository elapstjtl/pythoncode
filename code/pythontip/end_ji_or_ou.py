L = [2, 8, 3, 50]
count2 = 0
count5 = 0
for i in L:
    temp = i
    while i % 2==0 and i!=0:
        i = i/2
        count2+=1
    while temp % 5 == 0 and i!=0:
        temp = temp/5
        count5+=1
if count2 > count5:
    print(0)
else:
    print(1)
