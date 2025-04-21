n = int(input("Enter base:"))
e = int(input("Enter exponent:"))
p = 1
for i in range(1,e+1):
    p *= n
print(p)