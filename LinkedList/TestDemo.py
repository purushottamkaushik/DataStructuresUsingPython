n ,k = 4,6

lst = [0] * n
for j in range(n):
    lst[j] = int(input("Enter the number"))

for i in range(k):
    temp = lst[len(lst) -1 ]
    for j in range(n-1,0,-1):
        lst[j] = lst[j-1]
    lst[0] = temp    
    
for k in range(len(lst)):
    print(lst[k],end=" ")


    