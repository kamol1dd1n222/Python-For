son = int(input("Istalgan int son: "))
if son > 1:
    for i in range(1,son+1,1):
        print(i,end="  ")
else:
    for i in range(1,son-1,-1):
        print(i,end="  ")