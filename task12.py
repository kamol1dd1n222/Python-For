n =  int(input("N: "))
juft_yigindi = 0
toq_yigindi = 0
if n > 1:
    for i in range(1,n+1,1):
        if i % 2 == 0:
            juft_yigindi += i
        else:
            toq_yigindi += i
else: 
    for i in range(1,n-1,-1):
        if i % 2 == 0:
            juft_yigindi += i
        else:
            toq_yigindi += i
print("Toq yig'indi ==> ",toq_yigindi)
print("Juft yig'indi ==> ",juft_yigindi)