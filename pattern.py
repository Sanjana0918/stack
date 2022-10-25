num=int(input("Enter number of rows : "))
print("------Pattern 1------")
for i in range(0,num):
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")
print("------Pattern 2------")
for i in range(0,num):
    for j in range(0,2*i+1):
        print("*",end=" ")
    print("\n")
print("------Pattern 3------")
for i in range(num,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print("\n")
print("------Pattern 4------")
for i in range(0,num):
    for j in range(0,num-1-i):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")
print("------Pattern 5------")
for i in range(0,num):
    for j in range(0,i):
        print(end=" ")
    for j in range(num-i):
        print("*",end=" ")
    print("\n")
print("------Diamond pattern------")
for i in range(0,num):
    for j in range(0,num-1-i):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print("\n")
for i in range(0,num-1):
    for j in range(0,i+1):
        print(end=" ")
    for j in range(0,num-1-i):
        print("*",end=" ")
    print("\n")