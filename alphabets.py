#   A  pattern by nested loop

a = int(input())
for i in range(a+1):
    for j in range(a+1):
        if (j==0 or j==a) and (i!=0) or (i==0 or i==(a//2)+1) and (j<a and j>0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

