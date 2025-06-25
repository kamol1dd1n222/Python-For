son = int(input("Istalgan 15 dan kichik son: "))
if son < 15:
     for i in range(son,15+1,1):
        print(i,end="  ")
else: 
    for i in range(son,15-1,-1):
        print(i,end="  ")
   