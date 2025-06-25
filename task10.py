max_son = int(input("1 - son: "))
for i in  range(2,8,1):
    son = int(input(f"{i} - son: "))
    if son > max_son:
        max_son = son
print("Maximum son ==> ",max_son)