#Divisors

num = int(input("enter the number to be divided : "))

list_range = list(range(1,num+1))
list_div = []

for i in list_range:
    if num % i == 0:
        list_div.append(i)

print(list_div)        
