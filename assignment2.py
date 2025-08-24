

#program to print odd or even number
n= int(input("Enter a number: "))
if n % 2 == 0:
  print(n, "is an even number")
else:
  print(n, "is an odd number")


#sum of integers from 1 to 50
total_sum = 0 #initialize sum to 0
for i in range(1,51): # range(1, 51) goes from 1 to 50
  total_sum += i #add each number to total sum

print("The sum of numbers from 1 to 50 is:", total_sum)