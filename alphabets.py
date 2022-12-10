#   A  pattern by nested loop

a = int(input("enter R: "))
for i in range(a):
    for j in range(a+1):
        if (j==0 or j==a-1) and (i!=0) or (i==0 or i==(a//2)) and (j<a-1 and j>0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    print()
