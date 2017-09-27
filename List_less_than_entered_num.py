#To fetch less than any user entered number

a = [1,1,3,5,8,13,21,34,55,89]

num = int(input("Enter the number of your choice : "))

new_list = []

for i in a:
    if i < num :
        new_list.append(i)

print(new_list)
