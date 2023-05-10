
h = int(input("Enter the number "))
for i in range(h+1):
    j = 0
    for j in range(h-i):
        print(" ", end=" ")
    for j in range(2*i-1):
        print("*", end=" ")
    print()
