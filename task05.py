boshi = int(input("Boshlanish qiymati: "))
son = int(input("Tugash qiymati: "))
if boshi < son: 
    for i in range(boshi,son+1,1):
        print(i,end="  ")
else:
    for i in range(boshi,son-1,-1):
         print(i,end="  ")