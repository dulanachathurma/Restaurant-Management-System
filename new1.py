num1 = [23,45,67,78,89,34,67]
num2 = [34,56,78,90,12,34,56]

for i in num1:
    for j in num2:
        if i == j:
            print(i)
            
t = (1,2,3,40)
print(len(t))
print(min(t))
print(max(t))
print(sum(t))
print(sorted(t,reverse=True))


L =[]

for i in range(1,11):
    L.append(i)
print(L)
