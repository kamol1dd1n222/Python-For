son = int(input("Son: "))
step = int(input("Nechtadan qadam tashlasin: "))
if son < 15:
    for i in range(son,15+1,step):
        print(i,end="  ")
else:
    for i in range(son,15-1,-step):
        print(i,end="  ")