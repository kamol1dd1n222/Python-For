narx = float(input("1 -telefon narxi: "))
min_narx = narx
max_narx = narx
for i in range(2,6,1):
    narx2 = float(input(f"{i} - telefon narxi: "))
    if narx2 > max_narx:
        max_narx = narx2
    if narx2 < min_narx:
        min_narx = narx2
print("Minimum Narx - ",min_narx)
print("Maximum Narx - ",max_narx)