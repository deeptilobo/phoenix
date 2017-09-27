import datetime

now = datetime.datetime.now()

name = raw_input("enter your name : ")

age = int(input("enter you age : "))

n1 = 100 - age
yr = now.year
year = yr + n1

print("Hi " + name)
print("you will turn 100yrs in the year : " + str(year))
