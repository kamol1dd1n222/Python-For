son = int(input("Istalgan 15 dan kichik son: "))
if son >= 15:
    print("15 dan kichik son kiriting!!!")
else: 
    for i in range(son,15+1,1):
        print(i,end="  ")