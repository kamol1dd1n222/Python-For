n = int(input("N: "))
a = int(input("1-son: "))
max_son = a
min_son = a
for i in range(2,n+1,1):
    son = int(input(f"{i} - son: "))
    if son < min_son:
        min_son = son
    if son > max_son:
        max_son = son
print(max_son,"     ",min_son)    
ortacha_qiymat = (max_son + min_son) / 2
print(ortacha_qiymat)