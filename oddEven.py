#To find if a number is odd or even

num = int(input("Enter a number : "))

mod = num % 2

if mod > 0:
   print("You have entered an odd number.")
else:
   print("You have entered an even number.")
