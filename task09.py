min_son = int(input("1 - son: "))
for i in  range(2,8,1):
    son = int(input(f"{i} - son: "))
    if son < min_son:
        min_son = son
print("Minimum son ==> ",min_son)